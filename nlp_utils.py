import os
from typing import Dict, List, Tuple

import spacy


class EmotionDetector:
    """
    Lightweight rule-based emotion detector using spaCy tokenization and simple keyword cues.
    Returns one of: sadness, stress, anger, happiness, or unknown.
    """

    SUPPORTED_EMOTIONS: Tuple[str, ...] = (
        "sadness",
        "stress",
        "anger",
        "happiness",
        "unknown",
    )

    def __init__(self, model_name: str = "en_core_web_sm") -> None:
        # Load spaCy model once. If the package is installed via wheel, name is available.
        # Falls back to spacy.load which will raise if model is missing.
        self.nlp = spacy.load(model_name)

        # Define simple keyword lexicons. This is intentionally minimal and explainable.
        self.keywords: Dict[str, List[str]] = {
            "sadness": [
                "sad",
                "down",
                "depressed",
                "lonely",
                "tearful",
                "unhappy",
                "blue",
                "miserable",
                "heartbroken",
            ],
            "stress": [
                "stressed",
                "overwhelmed",
                "anxious",
                "pressure",
                "burned",
                "burnt",
                "deadline",
                "worry",
                "worried",
                "tense",
            ],
            "anger": [
                "angry",
                "mad",
                "furious",
                "rage",
                "irritated",
                "annoyed",
                "upset",
                "pissed",
            ],
            "happiness": [
                "happy",
                "joy",
                "excited",
                "grateful",
                "glad",
                "great",
                "delighted",
                "thrilled",
                "wonderful",
            ],
        }

    def detect_emotion(self, text: str) -> str:
        if not text or not text.strip():
            return "unknown"

        doc = self.nlp(text.lower())
        tokens = {token.lemma_ for token in doc if token.is_alpha}

        # Simple keyword matching by lemma
        scores: Dict[str, int] = {}
        for emotion, cues in self.keywords.items():
            scores[emotion] = sum(1 for cue in cues if cue in tokens)

        if not scores:
            return "unknown"

        # Choose the emotion with the highest score; if all zero, unknown
        top_emotion, top_score = max(scores.items(), key=lambda kv: kv[1])
        if top_score == 0:
            return "unknown"
        return top_emotion


def build_response_for_emotion(emotion: str) -> str:
    """Return an empathetic, supportive message based on the detected emotion."""
    if emotion == "sadness":
        return (
            "I’m sorry you’re feeling down. It might help to write your feelings in a journal, "
            "talk with a trusted friend, or take a gentle walk. You’re not alone—small steps count."
        )
    if emotion == "stress":
        return (
            "It sounds like things are overwhelming. Try a 4-7-8 breathing exercise, "
            "a 5-minute break, or listing your top 1–2 priorities. You’ve got this—one step at a time."
        )
    if emotion == "anger":
        return (
            "I hear a lot of frustration. Consider pausing for a few slow breaths, "
            "stepping away briefly, or jotting down what you can and can’t control right now."
        )
    if emotion == "happiness":
        return (
            "That’s wonderful to hear! Take a moment to celebrate—maybe share it with someone, "
            "note it in a gratitude list, or savor what made this moment special."
        )
    # unknown
    return (
        "Thanks for sharing. I’m here to support you. If you’d like, tell me a bit more about how you’re feeling, "
        "or try a short grounding exercise: name 5 things you can see, 4 you can touch, 3 you can hear, 2 you can smell, 1 you can taste."
    )


__all__ = ["EmotionDetector", "build_response_for_emotion"]

