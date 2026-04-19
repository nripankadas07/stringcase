import pytest
from stringcase import to_camel, to_pascal
from stringcase.errors import StringcaseError

def test_camel_empty(): assert to_camel("") == ""
def test_camel_snake(): assert to_camel("hello_world") == "helloWorld"
def test_camel_pascal(): assert to_camel("HelloWorld") == "helloWorld"
def test_camel_http(): assert to_camel("HTTPServer") == "httpServer"
def test_pascal_empty(): assert to_pascal("") == ""
def test_pascal_snake(): assert to_pascal("hello_world") == "HelloWorld"
def test_pascal_camel(): assert to_pascal("helloWorld") == "HelloWorld"
def test_pascal_http(): assert to_pascal("HTTPServer") == "HttpServer"
def test_camel_bad():
    with pytest.raises(StringcaseError): to_camel(None)
def test_pascal_bad():
    with pytest.raises(StringcaseError): to_pascal(None)
