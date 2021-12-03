from oplossing import kwadraat

def test1():
    result = KWADRATEREN(5).kwadraat()
    expected = 25
    assert result == expected


def test2():
    result = KWADRATEREN(20).kwadraat()
    expected = 400
    assert result == expected


def test3():
    result = KWADRATEREN(12).kwadraat()
    expected = 144
    assert result == expected


def test4():
    result = KWADRATEREN(1).kwadraat()
    expected = 1
    assert result == expected

