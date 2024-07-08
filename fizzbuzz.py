def func(x):
    if(x % 15 == 0):
        return('fizzbuzz')
    elif(x % 5 == 0):
        return 'buzz'
    elif(x % 3 == 0):
        return 'fizz'
    else:
        return x
