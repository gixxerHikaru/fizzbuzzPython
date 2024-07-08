from fizzbuzz import func

def test_入力値1の時出力値1():
    assert func(1) == 1

def test_入力値2の時出力値2():
    assert func(2) == 2

def test_入力値3の時出力値fizz():
    assert func(3) == 'fizz'

def test_入力値4の時出力値4():
    assert func(4) == 4
