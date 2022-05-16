def test_hello():
    greeting = "HELLO WORLD"
    assert greeting.capitalize() == 'Hello world'


def test_number_str():
    assert 1 == int("1")
