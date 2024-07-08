from fizzbuzz import func

def test_入力値1の時出力値1():
    assert func(1) == 1

def test_入力値2の時出力値2():
    assert func(2) == 2

def test_入力値3の時出力値fizz():
    assert func(3) == 'fizz'

def test_入力値4の時出力値4():
    assert func(4) == 4

def test_入力値5の時出力値buzz():
    assert func(5) == 'buzz'

def test_入力値6の時出力値fizz():
    assert func(6) == 'fizz'

def test_入力値7の時出力値7():
    assert func(7) == 7

def test_入力値8の時出力値8():
    assert func(8) == 8

def test_入力値9の時出力値fizz():
    assert func(9) == 'fizz'

def test_入力値10の時出力値buzz():
    assert func(10) == 'buzz'

def test_入力値11の時出力値11():
    assert func(11) == 11

def test_入力値12の時出力値fizz():
    assert func(12) == 'fizz'
