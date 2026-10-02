from calculator import add


def test_add():
    assert add(2, 3) == 5


def test_add_with_negative_operand():
    assert add(-2, 3) == 1
