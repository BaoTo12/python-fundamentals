# class MyClass:
#     x = 5


# p1 = MyClass()
# print(p1.x)
# print(type(p1))


#! Init method
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# p1 = Person("Chi Bao", 25)
# print(p1.name)
# print(p1.age)

#! The __str__() Method

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# p1 = Person("John", 36)

# print(p1)

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f"Hello {self.name}: {self.age}"

#     def myfunc(self):
#         print("Hello my name is " + self.name)


# p1 = Person("Bao", 24)

# p1.myfunc()


#! Inheritance
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

# Use the Person class to create an object, and then execute the printname method:


class Student(Person):
    def __init__(self, fname, lname):
        super().__init__( fname, lname)


s1 = Student("Thang", 24)

s1.printname()
