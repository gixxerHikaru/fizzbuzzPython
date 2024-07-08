def func(x):
    if(x % 15 == 0):
        return('fizzbuzz')
    elif(x % 5 == 0):
        print('buzz')
        return 'buzz'
    elif(x % 3 == 0):
        print('fizz')
        return 'fizz'
    else:
        print(x)
        return x
