def func(x):
    if(x % 5 == 0):
        print('buzz')
        return 'buzz'
    elif(x % 3 == 0):
        print('fizz')
        return 'fizz'
    else:
        print(x)
        return x
