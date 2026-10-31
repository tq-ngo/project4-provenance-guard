# Acceptance criteria — Provenance Guard

Five criteria that say what "working" means for this service, written in unit 7
**before** you built it.

**All five are yours.** None are given.

An acceptance criterion names a number or something plainly observable. *"The
detector is accurate"* is an opinion — and perfect AI detection isn't possible
anyway, so it's an opinion about something nobody can deliver. *"Of 10 pieces I
wrote myself, at most 1 is labelled high-confidence AI"* is a criterion.

Under each, write a sentence or two on **why that target**. *"I allow at most 1
false positive in 10 because on a writing site a wrong accusation costs more
than a missed detection"* is a real answer.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## Pick numbers you can defend

**Cover at least three of these five areas.** They're prompts, not a form.

| Area | A question it could answer |
|---|---|
| False positives | How often may a human's writing get called AI? |
| Score spread | How far apart should clearly-AI and clearly-human text score? |
| Label coverage | Is every one of your three labels actually reachable? |
| The appeal path | Does an appeal always change status and always get recorded? |
| Bad input | What happens when `text` is missing, empty, or enormous? |

Two things worth knowing before you pick numbers:

- **The expensive mistake is one-sided.** Missing some AI text costs the site a
  little. Accusing a real writer costs that person a lot. A criterion that
  treats both errors as equally bad is describing a system nobody would ship.
- **Unit 8 tests across three trials, and the target has to hold across all
  three.** Your first signal runs a model, so identical input can score
  differently twice. A target of "at most 1 in 10" against trials of 2, 1, 2 is
  a **miss**.

---
## 1. False positive rate on human writing

Of 10 distinct pieces of verified human-authored writing, at most 1 is labeled high-confidence AI (`guess == "ai"`) across each of the three evaluation trials.

**Why this target:**
On a writing platform or academic submission portal, a false accusation inflicts severe asymmetric harm on an honest author, destroying user trust and risking wrongful penalties. A 10% ceiling (at most 1 in 10) sets an enforceable safety standard that requires plain or non-native human writing to land in the "unsure" band rather than being falsely flagged as machine-generated.

---

## 2. Score spread between canonical AI and human text

The difference between the mean combined score of clearly AI-generated passages and the mean combined score of clearly human-authored passages must be at least 0.35 (`mean_ai_score - mean_human_score >= 0.35`).

**Why this target:**
A detector whose average scores cluster narrowly around the midpoint (e.g., 0.48 versus 0.52) offers virtually no discriminative value. Enforcing a minimum score spread of 0.35 ensures that canonical examples cleanly separate into the human and AI confidence bands rather than collapsing entirely into the unsure category.

---

## 3. Label reachability across all three tiers

Across an evaluation set of diverse test submissions, each of the three output labels (`high-confidence human`, `unsure`, and `high-confidence AI`) must be reached by at least 2 distinct submissions.

**Why this target:**
This proves there are no dead bands or threshold disconnects between `scoring.py` and `config.py`. If any of the three categories cannot be produced by real inputs, the classification tiers are poorly calibrated and the system fails to communicate uncertainty or confidence properly.

---

## 4. Deterministic appeal recording and state transition

100% of appeal requests submitted for a valid `content_id` with non-empty reasoning must return HTTP 200, set the status to `under_review`, and append an audit event to `logs/audit.jsonl`.

**Why this target:**
Procedural justice requires that once an author challenges a decision, their appeal is reliably recorded in the audit trail without fail. A silent failure or dropped appeal would leave a writer accused with no recourse, defeating the entire purpose of human-in-the-loop review.

---

## 5. Graceful rejection of malformed and extreme inputs

100% of malformed or extreme requests (missing `text` field, empty `text: ""`, `text: null`, non-string types, or text exceeding 50,000 characters) return an HTTP 400 Bad Request with a structured error JSON, and 0% result in an unhandled HTTP 500 server crash.

**Why this target:**
A production service inevitably encounters malformed payloads, scraper probes, and network truncation. Failing cleanly at the boundary with HTTP 400 protects service stability and prevents upstream callers from interpreting a crashed handler as a system outage.



---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 8 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath, like this:

         ## 2. Uncertain cases land in the unsure band

         The system handles uncertain cases well.

         **Why this target:** ...

         > **Revised in unit 8:** Text I judged borderline scores between
         > 0.4 and 0.6 in at least 4 of 5 cases.
         >
         > **Why revised:** "well" gave me nothing to check. I couldn't
         > reach a verdict from it at all.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "At most 1 of 10 of my own pieces flagged as AI" → "at most 3
            of 10", because 1 of 10 turned out to be hard.

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
     ───────────────────────────────────────────────────────────────────────── -->
