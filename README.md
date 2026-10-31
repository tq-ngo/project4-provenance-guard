# Provenance Guard

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first.**
>
> Once `python test.py` passes, in one terminal:
>
> ```bash
> python app.py
> ```
>
> and in another:
>
> ```bash
> curl -X POST http://127.0.0.1:5000/ping \
>   -H "Content-Type: application/json" \
>   -d '{"message": "hello"}'
> ```
>
> That's a web service. Something sent it text and it sent something back.
> Everything this unit is filling in the middle.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     Unit 7 asks for the first five sections. Unit 8 adds the five below.

     Everything is pasted as TEXT. A pasted curl response gets full credit;
     a picture of your terminal gets none.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 7 — THE BUILD ═══════════════════════ -->

## What This Does

When a submission arrives at Provenance Guard, it passes through seven sequential stages before a reader sees its final label:

1. **Ingestion & Validation (`app.py::submit`)**: The incoming JSON request is checked for valid `text` and `creator_id` fields. Payloads that are empty, malformed, or exceeding size bounds are rejected with HTTP 400.
2. **Identity Assignment**: The service generates a unique `content_id` (UUIDv4) that permanently binds the submission text, its audit trail, and any subsequent appeal.
3. **Signal 1 Evaluation (`detector.py::model_signal`)**: The local causal language model (`gpt2`) reads the text and evaluates its token-by-token perplexity (how predictable each word was given the preceding context), mapped to a 0.0–1.0 score where higher means more AI-like.
4. **Signal 2 Evaluation (`stylometry.py::style_signal`)**: The text is analyzed purely as text structure without considering semantic meaning. It computes sentence length variance (coefficient of variation), vocabulary richness (type-token ratio), and punctuation density, normalized into a 0.0–1.0 score where higher means more AI-like.
5. **Signal Combination (`scoring.py::combine_signals`)**: The two scores are combined using a weighted rule (60% model, 40% stylometry). If the two signals strongly diverge ($|\text{model\_score} - \text{style\_score}| \ge 0.40$), a disagreement dampener pulls the combined score toward 0.50 ("unsure") to prevent a false accusation.
6. **Empathetic Label Mapping (`scoring.py::score_to_label`)**: The combined score is mapped against thresholds (human $\le 0.35$, AI $\ge 0.65$, unsure between) into a machine-readable guess and a reader-facing natural language label written without technical jargon.
7. **Audit Logging & Response Dispatch (`audit.py::log_decision`)**: All nine required fields (`timestamp`, `content_id`, `creator_id`, `guess`, `model_score`, `style_score`, `combined_score`, `label`, `status="decided"`) are appended to `logs/audit.jsonl`, and an HTTP 200 JSON response containing both signal scores and the label is returned to the client.

---

## Signals and Scoring

<!-- For each signal: what property it measures, why that might differ between
     human and AI writing, and WHAT IT CAN'T SEE.

     The blind spot is not optional. If you can't name it you don't understand
     the signal yet — and unit 8's attack set is built out of blind spots. -->

### Signal one — the model signal

**What it measures:**
Token-level perplexity calculated by a local causal language model (`gpt2`). It measures how predictable each next token is based on standard English probability distributions, mapped via a logistic curve to a 0.0 to 1.0 score where higher means more predictable (more likely AI).

**Why that might differ between human and AI writing:**
Language models generate text by repeatedly selecting high-probability tokens from next-word distributions, resulting in low perplexity and high predictability. Human writing naturally wanders: it features idiosyncratic phrasing, unexpected word choices, abrupt tonal shifts, and domain-specific expressions that surprise the model.

**What it can't see:**
Predictability is not authorship. This signal cannot distinguish between an AI generating common phrases and an honest human writing plainly on purpose. Non-native English (ESL) writers, young students, or authors writing simple instructional or technical documentation use common words and standard sentence structures; `gpt2` finds them highly predictable and flags them as AI. Conversely, ornate, jargon-heavy, or highly stylized AI prose yields high perplexity and fools this signal into scoring it as human.

### Signal two — the style signal

**What it measures:**
The physical, structural surface geometry of the text across three metrics: sentence length spread (standard deviation of sentence length divided by the mean), lexical diversity (type-token ratio), and punctuation density (commas, semicolons, dashes, and quotes per 100 words).

**Why that might differ between human and AI writing:**
Autoregressive language models naturally produce uniform, evenly-cadenced sentences of medium length (15–22 words) with steady vocabulary recurrence. Human writing is inherently "lumpy": a three-word fragment often sits beside a 45-word compound sentence, accompanied by expressive punctuation like semicolons, em-dashes, and colons.

**What it can't see:**
This signal cannot read or comprehend meaning. It measures text only as shape and tokens. Any superficial modification that alters structure without changing content fools it: adding typos or misspellings artificially inflates vocabulary variety (type-token ratio), while inserting arbitrary line breaks or random exclamation marks warps sentence variance and punctuation density, causing AI text to register as human.

### The combining rule

<!-- Write the rule in words, then give the numbers. What happens when the two
     signals disagree? -->

**The rule:**
We compute a weighted average of the two signals (60% weight to Signal 1 because token perplexity across several hundred tokens provides a steadier baseline than short-sample syntax, and 40% weight to Signal 2). However, when the two signals strongly disagree ($|\text{model\_score} - \text{style\_score}| \ge 0.40$), the rule treats this divergence as epistemic uncertainty and pulls the combined score 50% towards the neutral midpoint (0.50). This guarantees that a single flawed signal cannot push an innocent writer past the AI threshold.

**The numbers:**
- `WEIGHT_MODEL_SIGNAL = 0.60`
- `WEIGHT_STYLE_SIGNAL = 0.40`
- `DISAGREEMENT_THRESHOLD = 0.40`
- `HUMAN_THRESHOLD = 0.35`
- `AI_THRESHOLD = 0.65`

Formula:
```python
weighted_avg = 0.60 * model_score + 0.40 * style_score
if abs(model_score - style_score) >= 0.40:
    combined_score = 0.50 * weighted_avg + 0.50 * 0.50
else:
    combined_score = weighted_avg
```

**Where it lives:** `scoring.py::combine_signals`

<!-- ⚠️ The grader checks your code against that line. If your rule lives
     somewhere else, say where. -->

**A case where my two signals split, and what my rule does with it:**
Consider plain, clear human writing (such as an essay by a non-native English speaker):
- Signal 1 (`model_score`): `0.80` (the vocabulary is basic and predictable to GPT-2).
- Signal 2 (`style_score`): `0.30` (the sentence lengths vary naturally between short points and long explanatory sentences).
The difference $|0.80 - 0.30| = 0.50 \ge 0.40$. A naive weighted average would yield $0.60 \times 0.80 + 0.40 \times 0.30 = 0.60$, dangerously close to an AI accusation. With our disagreement dampener:
$$\text{combined\_score} = 0.50 \times 0.60 + 0.50 \times 0.50 = 0.55$$
The score lands securely inside the `unsure` band ($0.35–0.65$), preventing an unfair AI accusation and allowing human review.



---

## Label Variants

<!-- The exact text of all three labels, as a reader would see them, and the
     score range each covers.

     Write them for someone who has never heard the word "threshold". -->

| Label | Score range | The exact text a reader sees |
|---|---|---|
| high-confidence human | 0.00 – 0.35 | This writing shows the natural rhythm, varied sentence structure, and vocabulary typical of human authorship. |
| unsure | 0.35 – 0.65 | We couldn't determine the origin of this text with confidence; it contains a blend of predictable patterns and stylistic variation. |
| high-confidence AI | 0.65 – 1.00 | This text closely reflects the uniform cadence and high predictability characteristic of AI-generated content. |

**Why I worded the "unsure" one this way:**
The "unsure" label must be explicitly non-accusatory because a substantial portion of text landing in this band is authored by real humans—specifically writers using clear, straightforward vocabulary or concise sentence structures. Phrasing it as "We couldn't determine the origin of this text with confidence" frames the result as a candid acknowledgment of the detector's limitations rather than a veiled suspicion of dishonesty. It completely avoids intimidating technical jargon ("thresholds", "perplexities", "0.52 probability") and emphasizes that human writing naturally exhibits both predictability and variation.



---

## Sample Run

<!-- One submission and one appeal, pasted as text: the request, the response,
     and the log entries. -->

**A submission**

<!-- The response needs content_id, guess, confidence, label, AND both
     signal scores - model_score and style_score. Unit 8's tools read those
     two off the response, so leaving them out costs you next unit's
     diagnostics. -->

```bash
$ curl -X POST http://127.0.0.1:5000/submit \
  -H "Content-Type: application/json" \
  -d '{"text": "...", "creator_id": "..."}'
```

```json

```

**An appeal**

```bash
$ curl -X POST http://127.0.0.1:5000/appeal \
  -H "Content-Type: application/json" \
  -d '{"content_id": "...", "reasoning": "..."}'
```

```json

```

**What the log shows afterwards**

```bash
$ curl "http://127.0.0.1:5000/log?limit=3"
```

```json

```

---

## How I Used AI

**Moment 1**

- *What I asked for:*
- *What came back:*
- *What I changed:*

**Moment 2**

- *What I asked for:*
- *What came back:*
- *What I changed:*

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** ___ per minute, ___ per day

**Why those numbers and not others:**
<!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->

**What a caller counts as:** <!-- per address, or per creator_id? They fail
differently — one script can look like a thousand callers, and one household
can look like one. -->

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

```

```

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->



**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

```json

```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:



---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

**Real output from one trial**, pasted as text, naming the file and function
that produced it:

```json

```

**Diagnoses**

<!-- For each miss AND each broken attack: the stage and the mechanism.

     Your service has five stages: the route, signal one, signal two, the
     combining rule, and the label mapping.

     Not a diagnosis:  "The evasion attacks got through."
     A diagnosis:      "Four evasion inputs got through. All four had typos
                        added to AI-generated text. My second signal measures
                        word variety, and typos raise word variety — so it read
                        them as more human. My combining rule weights that
                        signal at 0.6, so it dragged the whole score down."

     Look for a pattern. Five failures on one signal is one problem, not five. -->



---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Attack Run — After

<!-- Same format. `run_attacks.py --label after` -->



**Did it help, and how do I know:**

<!-- Widening the unsure band usually fixes one problem and creates another.
     Reporting that trade honestly is worth full credit. -->



---

## What's Still Broken

<!-- For each attack still getting through and each criterion still missed:
     what you'd do, and why you stopped. -->



**The trade I'd make if this ran for real:**

<!-- Two sentences. Fewer wrong accusations means more AI text getting through.
     Say which way you'd go and WHO PAYS FOR IT. -->



<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 7

       [ ] criteria.md has five numbered criteria, each naming a target
       [ ] Each has a reason underneath
       [ ] POST /submit returns content_id, guess, confidence, label,
           model_score and style_score
       [ ] Two signals that measure DIFFERENT things, each with a named blind spot
       [ ] Three label variants, all reachable, written out in full
       [ ] POST /appeal changes status and writes to the log
       [ ] Signals and Scoring names scoring.py::combine_signals
       [ ] Sample Run: a submission AND an appeal, as pasted text
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 8

       [ ] Rate limiting on /submit, with your numbers justified
       [ ] The pasted run of status codes showing 429
       [ ] Audit log with all nine fields, recording rejections too
       [ ] The attack set run IN FULL, every input with an outcome
       [ ] Ten audit log entries pasted as text
       [ ] Five criteria across three trials
       [ ] A diagnosis for every miss and every broken attack — stage AND mechanism
       [ ] One improvement, with Attack Run — After
       [ ] What's Still Broken, including the production trade
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
