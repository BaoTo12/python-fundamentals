# x = ("Apple", "Orange")
# l = list(x)
# l.append("CC")
# x = tuple(l)

# print(x)

# thistuple = ("apple", "banana", "cherry")
# y = ("orange",)
# thistuple += y

# print(thistuple)

# ! Unpack tuple
# x = ("apple", "banana")
# (a, banana) = x 
# print(a)
# print(banana)

# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

# (green, yellow, *red) = fruits

# print(green)
# print(yellow)
# print(type(red))

# fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

# (green, *tropic, red) = fruits

# print(green)
# print(tropic)
# print(red)

# ! loop in tuple
# thistuple = ("apple", "banana", "cherry")

# for var in thistuple:
#     print(var)

# thistuple = ("apple", "banana", "cherry")
# for index in range(len(thistuple)):
#     print(thistuple[index])

# thistuple = ("apple", "banana", "cherry")
# i = 0
# while i < len(thistuple):
#     print(thistuple[i])
#     i+=1

# ! Join two tuples
# tuple1 = ("a", "b" , "c")
# tuple2 = (1, 2, 3)

# tuple3 = tuple1 + tuple2
# print(tuple3)

# fruits = ("apple", "banana", "cherry")
# myT = fruits * 2

# print(myT)

#! tuple method
# thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

# x = thistuple.count(3)

# print(x)

x = ("apple", "banana")

result = x.index("apple")

print(result)