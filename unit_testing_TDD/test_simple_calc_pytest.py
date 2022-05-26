from simple_calc import SimpleCalc

def test_add():
    calc = SimpleCalc()
    actual = calc.add(4, 5)
    expected = 9
    assert actual == expected
