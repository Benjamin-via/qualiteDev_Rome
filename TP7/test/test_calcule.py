import calcule.calcule as c


def test_convertion():
    assert c.convertion('I') == 1
    assert c.convertion('V') == 5
    assert c.convertion('X') == 10
    assert c.convertion('L') == 50
    assert c.convertion('C') == 100
    assert c.convertion('D') == 500
    assert c.convertion('M') == 1000


def test_convertionSomme():
    assert c.convertionSomme('MMVI') == 2006
    assert c.convertionSomme('IV') == 4
    assert c.convertionSomme('MCMXLIV') == 1944


def test_calculatrice():

    assert c.calculatrice('+', 'III', 'MCMXLIV') == 1947
    assert c.calculatrice('-', 'VIII', 'VI') == 2
    assert c.calculatrice('*', 'V', 'V') == 25
    assert c.calculatrice('/', 'IV', 'II') == 2


def test_tradRomain():

    # MD = 1500 LM = 950 MMLD = 2450
    assert c.tradRomain('+', 'MD', 'LM') == 'MMCDL'
    assert c.tradRomain('+', 'M', 'MMCDIV') == 'MMMCDIV'