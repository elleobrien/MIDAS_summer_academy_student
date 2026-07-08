# arXiv Abstracts Corpus

A corpus of **2,091 recent arXiv abstracts** across six research fields, used in
**Day 4, Part 3** to teach embeddings, similarity, and topic modeling with BERTopic.

## Contents

| File | Description |
|------|-------------|
| `abstracts.csv` | The corpus: one row per paper. |
| `fetch_arxiv.py` | The script that built it (re-run to refresh or extend). |

## Columns

| Column | Meaning |
|--------|---------|
| `arxiv_id` | arXiv identifier (e.g. `2501.01234v1`). |
| `category` | arXiv subject category the paper was drawn from. |
| `field` | Friendly field label (the "ground truth" grouping). |
| `title` | Paper title. |
| `abstract` | Paper abstract (whitespace-normalized). |

## Fields

Roughly 350 abstracts each, drawn from the most recent submissions in each category:

| Field | arXiv category |
|-------|----------------|
| Astrophysics | `astro-ph.GA` |
| Machine Learning | `cs.LG` |
| Neuroscience | `q-bio.NC` |
| Materials Science | `cond-mat.mtrl-sci` |
| Econometrics | `econ.EM` |
| Atmospheric Science | `physics.ao-ph` |

The four physically distinct fields (astrophysics, materials, atmospheric,
econometrics) separate cleanly in embedding space. Machine learning and
neuroscience overlap in methods vocabulary ("model," "network," "data"), so they
break into finer sub-topics rather than one clean cluster each. That contrast is
intentional and makes for good classroom discussion.

## License

arXiv article **metadata** (titles and abstracts) is released under
[CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/) (public domain).
See the [arXiv API terms](https://info.arxiv.org/help/api/index.html) and
[bulk data access](https://info.arxiv.org/help/bulk_data.html). No API key is
required to query the arXiv API.

## Rebuilding

```bash
python fetch_arxiv.py
```

The script queries the public arXiv API (no key needed), keeps abstracts of at
least 400 characters, de-duplicates cross-listed papers, and writes
`abstracts.csv`. It sleeps 3 seconds between requests per arXiv's API guidance,
so a full rebuild takes a couple of minutes. Because it pulls the *most recent*
submissions, re-running it will produce a different (newer) set of papers.
