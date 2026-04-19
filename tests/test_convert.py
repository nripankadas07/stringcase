import pytest
from stringcase import convert
from stringcase.errors import StringcaseError

def test_snake(): assert convert("helloWorld", "snake") == "hello_world"
def test_camel(): assert convert("hello_world", "camel") == "helloWorld"
def test_pascal(): assert convert("hello_world", "pascal") == "HelloWorld"
def test_kebab(): assert convert("hello_world", "kebab") == "hello-world"
def test_constant(): assert convert("hello_world", "constant") == "HELLO_WORLD"
def test_dot(): assert convert("hello_world", "dot") == "hello.world"
def test_title(): assert convert("hello_world", "title") == "Hello World"
def test_path(): assert convert("hello_world", "path") == "hello/world"
def test_unknown():
    with pytest.raises(StringcaseError): convert("hello", "unknown")
def test_bad_input():
    with pytest.raises(StringcaseError): convert(None, "snake")
