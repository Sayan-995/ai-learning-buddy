def test_hello_world():
    # Simple hello world test
    assert "hello world" == "hello world"

def test_basic_math():
    # Basic math test
    assert 2 + 2 == 4
    assert 5 * 3 == 15

def test_string_operations():
    # Test string operations
    text = "AI Learning Buddy"
    assert len(text) > 0
    assert "AI" in text