import pytest
from stringcase import to_title, to_path
from stringcase.errors import StringcaseError

def test_title(): assert to_title("hello_world") == "Hello World"
def test_title_camel(): assert to_title("helloWorld") == "Hello World"
def test_title_http(): assert to_title("HTTPServer") == "Http Server"
def test_path(): assert to_path("hello_world") == "hello/world"
def test_path_camel(): assert to_path("helloWorld") == "hello/world"
def test_path_http(): assert to_path("HTTPServer") == "http/server"
def test_title_bad():
    with pytest.raises(StringcaseError): to_title(None)
def test_path_bad():
    with pytest.raises(StringcaseError): to_path(None)
