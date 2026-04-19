import pytest
from stringcase import split_words
from stringcase.errors import StringcaseError

def test_empty(): assert split_words("") == []
def test_single_lower(): assert split_words("hello") == ["hello"]
def test_snake(): assert split_words("hello_world") == ["hello", "world"]
def test_camel(): assert split_words("helloWorld") == ["hello", "world"]
def test_pascal(): assert split_words("HelloWorld") == ["hello", "world"]
def test_kebab(): assert split_words("hello-world") == ["hello", "world"]
def test_dot(): assert split_words("hello.world") == ["hello", "world"]
def test_path(): assert split_words("hello/world") == ["hello", "world"]
def test_http(): assert split_words("HTTPServer") == ["http", "server"]
def test_io(): assert split_words("IOError") == ["io", "error"]
def test_nums(): assert split_words("version2Release") == ["version2", "release"]
def test_unicode(): assert split_words("émigrésNaïve") == ["émigrés", "naïve"]
def test_bad_input():
    with pytest.raises(StringcaseError): split_words(None)
