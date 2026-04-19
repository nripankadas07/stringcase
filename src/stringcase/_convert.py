"""Internal case converters."""


def to_snake_case(words): return "_".join(words) if words else ""
def to_camel_case(words):
    if not words: return ""
    return words[0] + "".join(w.capitalize() for w in words[1:])
def to_pascal_case(words): return "".join(w.capitalize() for w in words) if words else ""
def to_kebab_case(words): return "-".join(words) if words else ""
def to_constant_case(words): return "_".join(w.upper() for w in words) if words else ""
def to_dot_case(words): return ".".join(words) if words else ""
def to_title_case(words): return " ".join(w.capitalize() for w in words) if words else ""
def to_path_case(words): return "/".join(words) if words else ""
