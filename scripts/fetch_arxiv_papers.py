#!/usr/bin/env python
import os
import textwrap
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.parse import quote_plus

import feedparser

BASE_URL = "http://export.arxiv.org/api/query"

# buckets aligned to blume-related topics
QUERIES = {
    "ner_extraction": [
        'all:"named entity recognition"',
        'all:"token classification"',
        'all:"span-based ner"',
        'all:"few shot ner"',
        'all:"weak supervision" AND all:"ner"'
    ],
    "entity_linking_graph": [
        'all:"entity linking"',
        'all:"knowledge graph" AND all:"construction"',
        'all:"entity disambiguation"',
        'all:"relation extraction"'
    ],
    "domain_adaptation": [
        'all:"domain adaptation" AND all:"nlp"',
        'all:"cross domain" AND all:"ner"',
        'all:"adapter" AND all:"transformer"'
    ],
    "retrieval_rag": [
        'all:"dense retrieval"',
        'all:"retrieval augmented generation"',
        'all:"hybrid retrieval"',
        'all:"neural search"'
    ],
}

# how many recent results per query to look at
MAX_RESULTS = 40

# look back this many days from now
LOOKBACK_DAYS = 1


CORE_KEYWORDS = [
    "named entity",
    "entity linking",
    "knowledge graph",
    "relation extraction",
    "information extraction",
    "retrieval-augmented",
    "retrieval augmented",
    "dense retrieval",
    "hybrid retrieval",
    "graph rag",
    "graphrag",
    "threat intelligence",
    "cybersecurity",
    "cyber security",
]


def build_url(query: str) -> str:
    q = f"{query} AND (cat:cs.CL OR cat:cs.LG OR cat:stat.ML)"
    return (
        f"{BASE_URL}?search_query={quote_plus(q)}"
        f"&start=0&max_results={MAX_RESULTS}"
        f"&sortBy=submittedDate&sortOrder=descending"
    )


def parse_published(entry):
    if hasattr(entry, "published_parsed") and entry.published_parsed:
        return datetime(*entry.published_parsed[:6], tzinfo=timezone.utc)
    if hasattr(entry, "updated_parsed") and entry.updated_parsed:
        return datetime(*entry.updated_parsed[:6], tzinfo=timezone.utc)
    return None


def shorten(text: str, max_len: int = 500) -> str:
    t = " ".join(text.split())
    if len(t) <= max_len:
        return t
    return t[: max_len - 3] + "..."


def fetch_bucket(name: str, queries: list, since: datetime):
    seen_ids = set()
    papers = []
    for q in queries:
        url = build_url(q)
        feed = feedparser.parse(url)
        for entry in feed.entries:
            arxiv_id = entry.get("id", "")
            if not arxiv_id or arxiv_id in seen_ids:
                continue
            published = parse_published(entry)
            if not published or published < since:
                continue
            seen_ids.add(arxiv_id)
            authors = [a.name for a in entry.get("authors", [])]
            summary = entry.get("summary", "")
            title = entry.get("title", "").replace("\n", " ").strip()
            link = entry.get("link", arxiv_id)
            cats = entry.get("tags", [])
            categories = [c["term"] for c in cats] if cats else []
            papers.append(
                {
                    "id": arxiv_id,
                    "bucket": name,
                    "title": title,
                    "authors": authors,
                    "summary": summary,
                    "link": link,
                    "categories": categories,
                    "published": published,
                    "query": q,
                }
            )
    papers.sort(key=lambda x: x["published"], reverse=True)
    return papers


def group_by_bucket(all_papers):
    buckets = {}
    for p in all_papers:
        buckets.setdefault(p["bucket"], []).append(p)
    return buckets


def score_paper(p):
    score = 0
    bucket = p.get("bucket", "")
    title = (p.get("title") or "").lower()
    summary = (p.get("summary") or "").lower()

    if bucket in ("ner_extraction", "entity_linking_graph"):
        score += 3
    elif bucket in ("domain_adaptation", "retrieval_rag"):
        score += 1

    for kw in CORE_KEYWORDS:
        if kw in title or kw in summary:
            score += 1

    return score


def format_markdown(all_papers, run_ts: datetime) -> str:
    if not all_papers:
        return f"# ML paper digest for {run_ts.date()}\n\n_no new papers in the last window._\n"

    for p in all_papers:
        p["score"] = score_paper(p)

    ranked = sorted(all_papers, key=lambda x: x["score"], reverse=True)
    top = [p for p in ranked if p["score"] > 0][:10]

    buckets = group_by_bucket(all_papers)
    lines = []
    lines.append(f"# ML paper digest for {run_ts.date()}\n")
    lines.append(f"_window: last {LOOKBACK_DAYS} days; generated at {run_ts.isoformat()}_\n")

    if top:
        lines.append("## Top picks for Blume\n")
        for p in top:
            pub_date = p["published"].strftime("%Y-%m-%d")
            lines.append(
                f"- [{p['title']}]({p['link']}) "
                f"(score={p['score']}, bucket={p['bucket']}, {pub_date})"
            )
        lines.append("")

    for bucket_name, papers in buckets.items():
        pretty = bucket_name.replace("_", " ").title()
        lines.append(f"## {pretty}\n")
        for p in papers:
            authors_str = ", ".join(p["authors"]) if p["authors"] else "unknown"
            cats_str = ", ".join(p["categories"]) if p["categories"] else "n/a"
            pub_date = p["published"].strftime("%Y-%m-%d")
            lines.append(f"### [{p['title']}]({p['link']})")
            lines.append(f"- id: `{p['id']}`")
            lines.append(f"- published: {pub_date}")
            lines.append(f"- authors: {authors_str}")
            lines.append(f"- categories: {cats_str}")
            lines.append(f"- query: `{p['query']}`")
            if "score" in p:
                lines.append(f"- blume_score: {p['score']}")
            summary = shorten(p["summary"])
            wrapped = textwrap.fill(summary, width=100)
            lines.append("")
            lines.append(wrapped)
            lines.append("")
        lines.append("")
    return "\n".join(lines)


def main():
    now = datetime.now(timezone.utc)
    since = now - timedelta(days=LOOKBACK_DAYS)

    all_papers = []
    for bucket, qs in QUERIES.items():
        papers = fetch_bucket(bucket, qs, since)
        all_papers.extend(papers)

    out_dir = Path("daily_papers")
    out_dir.mkdir(parents=True, exist_ok=True)

    md = format_markdown(all_papers, now)
    out_file = out_dir / f"{now.date()}.md"
    out_file.write_text(md, encoding="utf-8")

    latest_path = Path("LATEST_PAPERS.md")
    latest_path.write_text(md, encoding="utf-8")

    print(f"wrote {out_file} with {len(all_papers)} papers")
    if all_papers:
        print("buckets:", ", ".join(sorted({p["bucket"] for p in all_papers})))


if __name__ == "__main__":
    main()
