""" - Write a Python program to perform following operations on Lists :
a) Create and access list elements
b) Add and Remove list elements
c) Sort list element
d) Reverse list element
"""

# a) Create and access list elements

My_list = [1,3,5,2,4]
print("Original List :", My_list)

print("First Element :", My_list[0])
print("Last Element :", My_list[-1])


# b) Add and Remove list elements

My_list.append(60) # Add element at the end
print("After adding 60 :", My_list)

My_list.insert(2,25) # Insert element at index 2
print("After inserting 25 at index 2 :", My_list)

My_list.remove(3) # Remove element by value
print("After removing 3 :", My_list)

My_list.pop() # Remove last element
print("After popping last element :", My_list)


# c) Sort list elements

My_list.sort()
print("Sorted List :", My_list)


# d) Reverse List elements

My_list.reverse()
print("Reversed List :", My_list)
