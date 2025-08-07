# def myFunc(fname):
#     print(f"Hello World {fname}")

# myFunc("Chi Bao")

#! Arbitrary Arguments
# def my_function(*kids):
#     print("The youngest child is " + kids[2])


# my_function("Emil", "Tobias", "Linus")

#! Keyword argument

# def my_function(child1, **child2):
#     print(child1)
#     print(type(child2))

# my_function( "Chi", "asd", "asd")

# def my_function(firstName = "Chi bao" ,**kid):
#     print("His last name is " + kid["lname"])
#     print("His last name is " + firstName)


# my_function(firstName= "Bao" ,fname="Tobias", lname="Refsnes")


# def my_function(food):
#     for x in food:
#         print(x)


# fruits = ["apple", "banana", "cherry"]

# my_function(fruits)

#! Pass statement
# def my_func():
#     pass

# my_func()

#! Positional-Only Arguments
# def my_function(x, y, /):
#     print(x)
#     print(y)

# my_function(3, 5)

#! Keyword-Only Arguments

# def my_function(*, x):
#     print(x)


# my_function(x=3)

#! Combine Positional-Only and Keyword-Only

def my_function(a, b, /, *, c, d):
    print(a + b + c + d)


my_function(5, 6, c=7, d=8)
