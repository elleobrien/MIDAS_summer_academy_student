"""
Fetch a corpus of arXiv abstracts across several recognizable fields for the
Day 4 Part 3 embeddings/BERTopic lab (MIDAS Summer Academy).

arXiv article metadata (titles, abstracts) is distributed under CC0 1.0 (public
domain). See https://info.arxiv.org/help/api/index.html and
https://info.arxiv.org/help/bulk_data.html.

Uses only the Python standard library so it runs anywhere.
"""
import csv
import time
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET

API = "http://export.arxiv.org/api/query"
ATOM = "{http://www.w3.org/2005/Atom}"

# category -> friendly field label (the "ground truth" grouping)
CATEGORIES = {
    "astro-ph.GA": "Astrophysics",
    "cs.LG": "Machine Learning",
    "q-bio.NC": "Neuroscience",
    "cond-mat.mtrl-sci": "Materials Science",
    "econ.EM": "Econometrics",
    "physics.ao-ph": "Atmospheric Science",
}

PER_CATEGORY = 350          # target abstracts per field
PAGE = 100                  # arXiv API max per request is 100
MIN_ABSTRACT_CHARS = 400    # drop stubs so HDBSCAN has real content


def clean(text):
    return " ".join(text.split())


def fetch_category(cat, want):
    rows = []
    for start in range(0, want, PAGE):
        params = {
            "search_query": f"cat:{cat}",
            "start": start,
            "max_results": min(PAGE, want - start),
            "sortBy": "submittedDate",
            "sortOrder": "descending",
        }
        url = f"{API}?{urllib.parse.urlencode(params)}"
        with urllib.request.urlopen(url, timeout=60) as resp:
            data = resp.read()
        root = ET.fromstring(data)
        entries = root.findall(f"{ATOM}entry")
        if not entries:
            break
        for e in entries:
            arxiv_id = e.find(f"{ATOM}id").text.rsplit("/", 1)[-1]
            title = clean(e.find(f"{ATOM}title").text or "")
            abstract = clean(e.find(f"{ATOM}summary").text or "")
            if len(abstract) < MIN_ABSTRACT_CHARS:
                continue
            rows.append((arxiv_id, cat, CATEGORIES[cat], title, abstract))
        print(f"  {cat}: {len(rows)} kept after start={start}")
        time.sleep(3)  # arXiv API asks for >=3s between requests
    return rows


def main():
    all_rows = []
    for cat in CATEGORIES:
        print(f"Fetching {cat} ...")
        all_rows.extend(fetch_category(cat, PER_CATEGORY))

    # de-duplicate by id (a paper can be cross-listed)
    seen = set()
    deduped = []
    for r in all_rows:
        if r[0] in seen:
            continue
        seen.add(r[0])
        deduped.append(r)

    out = "abstracts.csv"
    with open(out, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["arxiv_id", "category", "field", "title", "abstract"])
        w.writerows(deduped)
    print(f"\nWrote {len(deduped)} abstracts to {out}")
    # per-field counts
    from collections import Counter
    for field, n in Counter(r[2] for r in deduped).most_common():
        print(f"  {field}: {n}")


if __name__ == "__main__":
    main()
