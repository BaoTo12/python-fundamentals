
#! Duplicates Not Allowed

# thisset = {"apple", "banana", "cherry", "apple"}
# print(thisset) 


# thisset = {"apple", "banana", "cherry", True, 1, 2}
# print(thisset)

#! Access items
# thisset = {"apple", "banana", "cherry"}
# print("banana" not in thisset)

#! Once set is created, you cannot change its item but can add new items
# thisset = {"apple", "banana", "cherry"}

# thisset.add("orange")

# print(thisset) 

# thisset = {"apple", "banana", "cherry"}
# tropical = {"pineapple", "mango", "papaya"}

# thisset.update(tropical)

# print(thisset)

#! Remove items from set
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)