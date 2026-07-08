# Real Abstracts Corpus

30 **real, open-access research abstracts** from behavioral and health psychology,
used in **Day 4, Part 2b** for a content-analysis exercise: coding each abstract for a
set of methodological features and then confronting how you would *validate* those codes
when there is no answer key.

Unlike a synthetic corpus, these are genuine published abstracts. They are messier,
carry real jargon and scale names, and, crucially, the interpretive judgments have **no
objective ground truth**. That is the point (see below).

## Files

| File | What it is |
|---|---|
| `abstracts.csv` | The corpus. Columns: `abstract_id`, `abstract`. |
| `attributions.csv` | Source and license for every abstract: title, authors, journal, year, DOI, license, URL. |

## Licensing and attribution

Every abstract is redistributed under its original **Creative Commons license** (CC BY or
CC0), which permits reuse with attribution. Each abstract remains © its authors; full
attribution for each item is in `attributions.csv`. Sourced from the Europe PMC
open-access subset, filtered to CC-BY/CC0 primary studies, with HTML stripped.

## There is deliberately no answer key

The synthetic version of this exercise shipped with a gold-standard key, which made
"accuracy" easy to measure but unrealistic. Real content analysis rarely has that luxury.
For the interpretive features here (`makes_causal_claim`, `overclaims`) there is **no
objective ground truth**: careful human coders disagree. Building a trustworthy key would
require multiple expert coders, adjudication, and an inter-rater agreement analysis. That
labor is exactly what the exercise is meant to expose, so this corpus ships without a key
on purpose.

## Features coded in the exercise

| Feature | Type | Difficulty |
|---|---|---|
| `sample_size` | reported N, or none | Easy (a fact in the text) |
| `population` | who the participants were | Medium |
| `study_design` | experimental / correlational / survey / other | Medium, interpretive |
| `makes_causal_claim` | does the conclusion assert causation, vs. only association | Hard (judgment) |
| `overclaims` | does the causal/actionable claim exceed what the design supports | Hardest (deep judgment) |

## Overclaiming: rubric for discussion (not labels)

`overclaims` is the headline judgment and the reason this task is hard. A working rubric:

- **Experimental (randomized) design + causal claim** → not overclaiming (the design
  supports causal language).
- **Correlational/cross-sectional design + associational conclusion** ("was associated
  with," "correlated with") → not overclaiming (appropriately cautious).
- **Correlational design + causal or prescriptive conclusion** ("X reduces Y," "reducing
  X would improve Y," "X drives Y") → overclaiming.
- **"Predicts / predictor"** in the regression sense is borderline; default to
  not-overclaiming unless paired with causal or actionable framing.
- Explicit hedges ("longitudinal research is needed," "we cannot infer causation") pull
  toward not-overclaiming, but a single abstract can hedge in one sentence and overclaim
  in another. Those mixed cases are where coders genuinely disagree.

Reasonable people will code some of these abstracts differently. Treat that disagreement
as the subject of the lesson, not a defect.
