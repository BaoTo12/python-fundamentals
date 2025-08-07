
#! Date time
# import datetime

# x = datetime.datetime.now()

# print(x)
# print(x.year)
# print(x.strftime("%A"))
# print(x.strftime("%B"))

#! Math
# x = min(5, 10, 25)
# y = max(5, 10, 25)

# print(x)
# print(y)

#! Json

# import json

# # some JSON:
# x =  { "name":"John", "age":30, "city":"New York"}

# # parse x:
# y = json.dumps(x)

# # the result is a Python dictionary:
# print(y)


#! PIP
# import camelcase

# c = camelcase.CamelCase()

# txt = "hello world"

# print(c.hump(txt))

#! Exception

# try:
#     print(x)
# except:
#     print("An exception occurred")

# print(x)

# try:
#     print("Hello")
# except:
#     print("Something went wrong")
# else:
#     print("Nothing went wrong")


#! Format string
# price = 59
# txt = f"The price is {price:.2f} dollars"
# print(txt)

# ? If else
# price = 49
# txt = f"It is very {'Expensive' if price > 50 else 'Cheap'}"

# print(txt)

# price = 59000
# txt = f"The price is {price:,} dollars"
# print(txt)

# price = 49
# txt = "The price is {} dollars"
# print(txt.format(price))

#! Type hint

# def say_hi(name: str) -> str:
#     return f'Hi {name}'


# greeting = say_hi('John')
# print(greeting)

# def say_hi(name: str) -> str:
#     return f'Hi {name}'


# greeting = say_hi(123)
# print(greeting)

# name : str = "John"
# name = 10

from typing import Union, List, Literal, Final

number = Union[float, int]


def add(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
    return x + y


def add1(x: int | float, y: int | float) -> int | float:
    return x + y


def add2(x: number, y: number) -> number:
    return x + y


#! Typing alias for list
ratings: List[int] = [1, 2, 3]
# ratings = {1: 'Bad', 2: 'average', 3: 'Good'}

def set_mode(mode: Literal["read", "write"]) -> None:
    print(f"Setting mode to {mode}")
    

set_mode("read")

HTTPS: Final[bool] = True 