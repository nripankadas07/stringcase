"""stringcase: Convert between common string case conventions."""

from stringcase.api import (to_snake, to_camel, to_pascal, to_kebab, to_constant, to_dot, to_title, to_path, split_words, convert)
from stringcase.errors import StringcaseError

__version__ = "0.1.0"
__all__ = ["to_snake", "to_camel", "to_pascal", "to_kebab", "to_constant", "to_dot", "to_title", "to_path", "split_words", "convert", "StringcaseError"]
