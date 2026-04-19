import pytest
from stringcase import to_kebab, to_constant, to_dot
from stringcase.errors import StringcaseError

def test_kebab(): assert to_kebab("helloWorld") == "hello-world"
def test_kebab_snake(): assert to_kebab("hello_world") == "hello-world"
def test_kebab_http(): assert to_kebab("HTTPServer") == "http-server"
def test_constant(): assert to_constant("helloWorld") == "HELLO_WORLD"
def test_constant_snake(): assert to_constant("hello_world") == "HELLO_WORLD"
def test_constant_http(): assert to_constant("HTTPServer") == "HTTP_SERVER"
def test_dot(): assert to_dot("helloWorld") == "hello.world"
def test_dot_snake(): assert to_dot("hello_world") == "hello.world"
def test_dot_http(): assert to_dot("HTTPServer") == "http.server"
def test_kebab_bad():
    with pytest.raises(StringcaseError): to_kebab(None)
def test_constant_bad():
    with pytest.raises(StringcaseError): to_constant(None)
def test_dot_bad():
    with pytest.raises(StringcaseError): to_dot(None)
