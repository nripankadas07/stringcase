"""Internal word tokenization logic."""

import re
from stringcase.errors import StringcaseError


def split_words(text: str) -> list[str]:
    if not isinstance(text, str):
        raise StringcaseError(f"Input must be a string, not {type(text).__name__}")
    if not text:
        return []
    marked = _insert_markers(text)
    words = _split_on_markers(marked)
    return [w.lower() for w in words if w]


def _insert_markers(text: str) -> str:
    result = []
    for i, ch in enumerate(text):
        if i > 0:
            prev_ch = text[i - 1]
            if prev_ch.islower() and ch.isupper():
                result.append("|")
            elif prev_ch.isdigit() and ch.isalpha():
                result.append("|")
            elif (i + 1 < len(text) and ch.isupper() and text[i + 1].islower() and prev_ch.isupper()):
                result.append("|")
                result.append(ch)
                continue
        result.append(ch)
    return "".join(result)


def _split_on_markers(text: str) -> list[str]:
    words = text.split("|")
    final_words = []
    for word in words:
        cleaned = re.sub(r"[_\-./\s]+", " ", word)
        parts = cleaned.split()
        final_words.extend(parts)
    return final_words
