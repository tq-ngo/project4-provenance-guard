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


def combine_signals(
    model_score: float,
    style_score: float,
    discourse_score: float | None = None,
) -> float:
    """
    Combine signals into one 0–1 score.

    Supports both 2-signal baseline (Unit 7) and 3-signal fusion (Stretch Feature 1).
    When discourse_score is None, uses 60% model / 40% style.
    When discourse_score is provided, uses 50% model / 30% style / 20% discourse.
    """
    if discourse_score is None:
        weighted_avg = 0.60 * model_score + 0.40 * style_score
    else:
        w_model = getattr(config, "WEIGHT_MODEL_SIGNAL", 0.50)
        w_style = getattr(config, "WEIGHT_STYLE_SIGNAL", 0.30)
        w_disc = getattr(config, "WEIGHT_DISCOURSE_SIGNAL", 0.20)
        weighted_avg = w_model * model_score + w_style * style_score + w_disc * discourse_score

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
