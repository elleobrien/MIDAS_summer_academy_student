# Real Abstracts Corpus

30 **real, open-access research abstracts** from behavioral and health psychology,
used in **Day 4, Part 2b** for a feature-extraction exercise: prompting an LLM to code
each abstract for methodological features, reading the outputs to find failures and
ambiguities, and sharpening the prompt in response.

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
For the interpretive feature here (`includes_causal_claim`) there is **no objective
ground truth**: careful human coders disagree. Building a trustworthy key would require
multiple expert coders, adjudication, and an inter-rater agreement analysis. That labor
is exactly what the exercise is meant to expose, so this corpus ships without a key on
purpose.

## Features coded in the exercise

| Feature | Type | Difficulty |
|---|---|---|
| `sample_size` | reported N, or none | Looks easy; ambiguous when enrolled and analyzed samples differ |
| `population` | who the participants were | Medium |
| `method` | experimental / correlational / other | Medium, interpretive |
| `includes_causal_claim` | does the conclusion assert causation, vs. only association | Hard (judgment) |

## The exercise subset

The notebook works with 5 abstracts chosen so that at least one failure or ambiguity is
likely under a bare, definition-free prompt:

| ID | Why it is in the subset |
|---|---|
| ABS-001 | cross-sectional questionnaire study; is that `correlational` or `other`? |
| ABS-002 | clean randomized experiment; the easy baseline case |
| ABS-005 | reports 167 randomized but 98 analyzed; which is `sample_size`? |
| ABS-006 | "predictive effect" language plus a prescriptive conclusion; borderline causal claim |
| ABS-023 | cross-sectional design that concludes screen exposure "affects" sleep and must be reduced |

## Causal-claim language: rubric for discussion (not labels)

`includes_causal_claim` asks whether a causal claim *is made*, not whether the design
justifies it. A working rubric:

- **Causal verbs** ("causes," "increases," "reduces," "improves," "leads to") in the
  conclusion → a causal claim.
- **Prescriptive conclusions** ("reducing X would improve Y," "interventions should
  target X") → a causal claim, since acting on X only makes sense if X changes Y.
- **Associational language** ("was associated with," "correlated with," "linked to")
  → not a causal claim.
- **"Predicts / predictor"** in the regression sense is borderline; the notebook's v2
  prompt codes it as association unless paired with causal or actionable framing.
- A single abstract can hedge in one sentence and claim in the next. Those mixed cases
  are where coders genuinely disagree.

Reasonable people will code some of these abstracts differently. Treat that disagreement
as the subject of the lesson, not a defect.
