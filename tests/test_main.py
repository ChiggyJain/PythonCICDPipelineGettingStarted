from src.main import addTwoNumbers

def test_addTwoNumbers():
    assert addTwoNumbers(2, 3) == 5
    assert addTwoNumbers(-1, 1) == 0
    assert addTwoNumbers(0, 0) == 0
    assert addTwoNumbers(1.5, 2.5) == 4.1