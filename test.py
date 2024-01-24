from main import calculate

def test(x, y):
    result = calculate(x, y)
    test_result = x + y
    assert result == test_result

test(5, 5)
test(7, 7)