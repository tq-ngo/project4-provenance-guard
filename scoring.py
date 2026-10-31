"""
Turning two numbers into one, and one number into something a person can read.
← YOU BUILD THIS IN MILESTONES 4 AND 5

Two functions live here, and both are stubs.

`combine_signals` is where your false-positive decision from Milestone 1
actually gets made. Everything above it — the labels, the appeal path — is
downstream of a number this function produced.

`score_to_label` is where you stop writing for a machine and start writing for
a person. A score of 0.62 means nothing to a writer.

⚠️ Your README's **Signals and Scoring** section has to name the file and
function holding your combining rule. The grader checks your code against what
you claim, so that line should read `scoring.py::combine_signals`.
"""

import config


def combine_signals(model_score: float, style_score: float) -> float:
    """
    Combine two 0–1 signals into one 0–1 score.

    Uses weighted combination with disagreement damping:
      1. Baseline weighted average using config.WEIGHT_MODEL_SIGNAL and config.WEIGHT_STYLE_SIGNAL.
      2. If signals disagree strongly (|model_score - style_score| >= config.DISAGREEMENT_THRESHOLD),
         the score is pulled 50% toward 0.50 (unsure midpoint) to guard against false accusations.
    """
    weighted_avg = (
        config.WEIGHT_MODEL_SIGNAL * model_score
        + config.WEIGHT_STYLE_SIGNAL * style_score
    )
    diff = abs(model_score - style_score)
    threshold = getattr(config, "DISAGREEMENT_THRESHOLD", 0.40)
    if diff >= threshold:
        combined = 0.50 * weighted_avg + 0.50 * 0.50
    else:
        combined = weighted_avg
    return round(min(max(combined, 0.0), 1.0), 4)


def score_to_label(score: float) -> tuple[str, str]:
    """
    Turn a score into a guess and the text a reader actually sees.

    Returns:
        (guess, label_text) — where `guess` is a short machine-readable string
        like "ai" / "human" / "unsure", and `label_text` is the full sentence
        shown to a person.
    """
    if score >= config.AI_THRESHOLD:
        return "ai", "This text closely reflects the uniform cadence and high predictability characteristic of AI-generated content."
    if score <= config.HUMAN_THRESHOLD:
        return "human", "This writing shows the natural rhythm, varied sentence structure, and vocabulary typical of human authorship."
    return "unsure", "We couldn't determine the origin of this text with confidence; it contains a blend of predictable patterns and stylistic variation."


def label_ranges() -> list[tuple[str, str]]:
    """
    The score range each label covers. Your README needs these beside the
    label text — given to you so the numbers can't drift apart from config.py.
    """
    return [
        ("high-confidence human", f"0.00 – {config.HUMAN_THRESHOLD:.2f}"),
        ("unsure", f"{config.HUMAN_THRESHOLD:.2f} – {config.AI_THRESHOLD:.2f}"),
        ("high-confidence AI", f"{config.AI_THRESHOLD:.2f} – 1.00"),
    ]
