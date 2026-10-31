"""
Signal two: the style signal. ← YOU BUILD THIS IN MILESTONE 4

Signal one reads the text for meaning. This one measures it *as text* — the
shape of it, without understanding a word.

Three measures are stubbed below because the brief names those three. They are
stubs, not implementations: what they compute is yours, and so is how you
combine them.

    sentence_length_spread   do sentences vary in length, or march in step?
    type_token_ratio         how much of the vocabulary repeats?
    punctuation_density      how much punctuation, and how varied?

Why these might differ between human and AI writing: generated prose tends
toward even, mid-length sentences and a narrower band of vocabulary, because
that's what "most likely next word" produces on average. Human writing is
lumpier — a three-word sentence next to a forty-word one.

⚠️ **The blind spot, which you have to name in Milestone 1.**

This signal cannot read. It has no idea what the text says. Anything that
changes the shape without changing the substance moves it — adding typos,
breaking up sentences, pasting in a quotation. That is a very cheap thing for
someone to do on purpose, and unit 8's attack set will do it to you.

Build each function on its own and call it from a terminal before you wire
anything together:

    python stylometry.py "some text to look at"
"""

import re
import statistics


def sentences(text: str) -> list[str]:
    """Split into sentences. Rough and good enough — given to you."""
    parts = re.split(r"(?<=[.!?])\s+", text.strip())
    return [p for p in parts if p.strip()]


def words(text: str) -> list[str]:
    """Split into lowercase words, punctuation stripped. Given to you."""
    return re.findall(r"[a-z0-9']+", text.lower())


# ── The three measures — YOU BUILD THESE ─────────────────────────────────────

def sentence_length_spread(text: str) -> float:
    """
    How much sentence length varies.

    Returns:
        A float representing the Coefficient of Variation (stdev / mean) of sentence lengths.
        Higher value indicates more cadence variation (characteristic of human writing).
        For text with fewer than 2 sentences, returns 0.0.
    """
    s_list = sentences(text)
    if len(s_list) < 2:
        return 0.0
    lens = [len(words(s)) for s in s_list]
    m = statistics.mean(lens)
    if m == 0:
        return 0.0
    return round(statistics.stdev(lens) / m, 4)


def type_token_ratio(text: str) -> float:
    """
    Unique words over total words.

    Returns:
        A float between 0 and 1. Higher means more varied vocabulary.
    """
    w = words(text)
    if not w:
        return 0.0
    return round(len(set(w)) / len(w), 4)


def punctuation_density(text: str) -> float:
    """
    How much punctuation, relative to length.

    Returns:
        A float representing punctuation mark count per 100 words.
    """
    w = words(text)
    if not w:
        return 0.0
    marks = re.findall(r'[,;:—–\-\"\'\(\)\!\?]', text)
    return round((len(marks) / len(w)) * 100.0, 4)


# ── Combining them ───────────────────────────────────────────────────────────

def style_signal(text: str) -> float:
    """
    The style signal as a 0–1 score. **Higher means more likely AI.**

    Combines sentence length spread, type-token ratio, and punctuation density:
      1. Low sentence spread (uniform lengths) indicates AI; high spread indicates human.
      2. Low TTR (repetitive vocabulary) indicates AI; high TTR indicates human.
      3. Absence of expressive punctuation (semicolons, em dashes, colons) indicates AI.
    """
    s_list = sentences(text)
    w_list = words(text)
    if not w_list:
        return 0.50

    # 1. Spread score: High CV (>= 0.70) -> human (0.0). Low CV (<= 0.15) -> AI (1.0).
    cv = sentence_length_spread(text)
    if len(s_list) < 2:
        ai_spread = 0.50
    else:
        ai_spread = max(0.0, min(1.0, 1.0 - (cv - 0.15) / 0.55))

    # 2. Vocabulary diversity score: High TTR (>= 0.80) -> human (0.0). Low TTR (<= 0.45) -> AI (1.0).
    ttr = type_token_ratio(text)
    ai_ttr = max(0.0, min(1.0, 1.0 - (ttr - 0.45) / 0.35))

    # 3. Punctuation score: Expressive marks (semicolon, dash, colon) signal human author.
    expressive = len(re.findall(r'[;:—–]', text))
    p_density = punctuation_density(text)
    if expressive > 0 or p_density > 18.0:
        ai_punct = 0.25
    elif p_density < 4.0:
        ai_punct = 0.50
    else:
        ai_punct = 0.65

    score = 0.45 * ai_spread + 0.35 * ai_ttr + 0.20 * ai_punct
    return round(max(0.0, min(1.0, score)), 4)


if __name__ == "__main__":
    import sys

    text = " ".join(sys.argv[1:]) or (
        "The system works well. It handles most cases correctly and provides "
        "good results. Users generally find it easy to use and understand."
    )

    print(f"{len(sentences(text))} sentences, {len(words(text))} words\n")
    print(f"sentence_length_spread   {sentence_length_spread(text)}")
    print(f"type_token_ratio         {type_token_ratio(text)}")
    print(f"punctuation_density      {punctuation_density(text)}")
    print(f"style_signal             {style_signal(text)}   (higher = more likely AI)")
    print("\nAll zeros? These are stubs — Milestone 4 is where you build them.")
