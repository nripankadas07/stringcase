import pytest
from stringcase import to_snake
from stringcase.errors import StringcaseError

def test_empty(): assert to_snake("") == ""
def test_camel(): assert to_snake("helloWorld") == "hello_world"
def test_pascal(): assert to_snake("HelloWorld") == "hello_world"
def test_kebab(): assert to_snake("hello-world") == "hello_world"
def test_http(): assert to_snake("HTTPServer") == "http_server"
def test_io(): assert to_snake("IOError") == "io_error"
def test_numbers(): assert to_snake("version2Release") == "version2_release"
def test_bad_input():
    with pytest.raises(StringcaseError): to_snake(None)
