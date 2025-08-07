
# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.
# SYNTAX: lambda arguments : expression

# def x(a, b): return a * b


# print(x(5, 6))

def myfunc(n):
    return lambda a: a * n

func =  myfunc(10)


print(func(2))