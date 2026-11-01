"""
Signal three: Discourse & Transition Marker Density.

Measures the presence of formulaic discourse transitions and repetitive n-gram
patterns disproportionately found in LLM-generated prose.
"""

import re

# Characteristic transitional words and phrases heavily favored by language models
LLM_MARKERS = [
    r"\bmoreover\b",
    r"\bfurthermore\b",
    r"\badditionally\b",
    r"\bin conclusion\b",
    r"\bto summarize\b",
    r"\bin summary\b",
    r"\bit is important to note\b",
    r"\bit is worth noting\b",
    r"\bcrucial role\b",
    r"\bvital role\b",
    r"\bkey factor\b",
    r"\btestament to\b",
    r"\bdelve into\b",
    r"\bdelves into\b",
    r"\bmultifaceted\b",
    r"\bnuanced\b",
    r"\bfirst and foremost\b",
    r"\bconsequently\b",
    r"\bsubsequently\b",
    r"\boverall\b",
    r"\bfirstly\b",
    r"\bsecondly\b",
    r"\bnotably\b",
]


def words(text: str) -> list[str]:
    """Extract lowercase words."""
    return re.findall(r"[a-z0-9']+", text.lower())


def marker_density(text: str) -> float:
    """
    Count formulaic LLM transition markers per 100 words.
    """
    w_list = words(text)
    if not w_list:
        return 0.0

    lower = text.lower()
    count = 0
    for pattern in LLM_MARKERS:
        count += len(re.findall(pattern, lower))

    return round((count / len(w_list)) * 100.0, 4)


def bigram_repetition(text: str) -> float:
    """
    Proportion of repeated bigrams. Higher means more repetitive phrasing.
    """
    w_list = words(text)
    if len(w_list) < 4:
        return 0.0

    bigrams = [f"{w_list[i]} {w_list[i+1]}" for i in range(len(w_list) - 1)]
    unique_bigrams = set(bigrams)
    repetition = (len(bigrams) - len(unique_bigrams)) / len(bigrams)
    return round(repetition, 4)


def discourse_signal(text: str) -> float:
    """
    The discourse signal as a 0–1 score. Higher means more likely AI.
    """
    w_list = words(text)
    if not w_list:
        return 0.50

    m_density = marker_density(text)
    b_rep = bigram_repetition(text)

    # 1. Marker score:
    # 0.0 markers/100 words -> 0.0 (human-like)
    # 2.5+ markers/100 words -> 1.0 (AI-like)
    marker_score = min(1.0, max(0.0, m_density / 2.5))

    # 2. Bigram repetition score:
    # Repetition scaling:
    rep_score = min(1.0, max(0.0, b_rep / 0.20))

    # Composite: 75% transition markers, 25% bigram repetition
    score = 0.75 * marker_score + 0.25 * rep_score
    return round(max(0.0, min(1.0, score)), 4)


if __name__ == "__main__":
    import sys

    text = " ".join(sys.argv[1:]) or (
        "Furthermore, it is important to note that the proposed framework plays a crucial "
        "role. Moreover, additionally, in conclusion, the results are multifaceted."
    )
    print(f"words:             {len(words(text))}")
    print(f"marker_density:    {marker_density(text)} per 100 words")
    print(f"bigram_repetition: {bigram_repetition(text)}")
    print(f"discourse_signal:  {discourse_signal(text)} (higher = more likely AI)")
