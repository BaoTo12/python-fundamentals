
#! Else in while loop
# ? With the else statement we can run a block of code once when the condition no longer is true:
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")

#!Else in For Loop
#? The else keyword in a for loop specifies a block of code to be executed when the loop is finished:
for x in range(6):
    print(x)
else:
    print("Finally finished!")
