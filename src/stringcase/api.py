"""Public API for stringcase."""

from stringcase._tokenize import split_words as _split_words
from stringcase._convert import (to_snake_case, to_camel_case, to_pascal_case, to_kebab_case, to_constant_case, to_dot_case, to_title_case, to_path_case)
from stringcase.errors import StringcaseError


def split_words(text: str) -> list[str]:
    return _split_words(text)


def _check(text):
    if not isinstance(text, str):
        raise StringcaseError(f"Input must be a string, not {type(text).__name__}")


def to_snake(text: str) -> str: _check(text); return to_snake_case(_split_words(text))
def to_camel(text: str) -> str: _check(text); return to_camel_case(_split_words(text))
def to_pascal(text: str) -> str: _check(text); return to_pascal_case(_split_words(text))
def to_kebab(text: str) -> str: _check(text); return to_kebab_case(_split_words(text))
def to_constant(text: str) -> str: _check(text); return to_constant_case(_split_words(text))
def to_dot(text: str) -> str: _check(text); return to_dot_case(_split_words(text))
def to_title(text: str) -> str: _check(text); return to_title_case(_split_words(text))
def to_path(text: str) -> str: _check(text); return to_path_case(_split_words(text))


def convert(text: str, style: str) -> str:
    _check(text)
    if not isinstance(style, str):
        raise StringcaseError(f"Style must be a string, not {type(style).__name__}")
    style_map = {"snake": to_snake, "camel": to_camel, "pascal": to_pascal, "kebab": to_kebab, "constant": to_constant, "dot": to_dot, "title": to_title, "path": to_path}
    if style not in style_map:
        raise StringcaseError(f"Unknown style '{style}'. Valid styles: {', '.join(style_map.keys())}")
    return style_map[style](text)
