"""
Write a python program to perform following operations on Tuples :
a) Create and access a Tuple
b) Nested Tuple
c) Repetition of Tuple
d) Concatenation of Tuples
"""

# a) Create and access a Tuple

Tup1 = (10,20,30,40,50)
print("Tuple :", Tup1)
print("First Element :", Tup1[0])
print("Last Element :", Tup1[-1])


# b) Nested Tuple

Tup2 = (1,2,(3,4,5),6)
print("Nested Tuple :", Tup2)
print("Access Nested Element :", Tup2[2][1])


# c) Repetition of Tuple

Tup3 = ('A','B')
Repeated_tuple = Tup3*3
print("Original Tuple :", Tup3)
print("Repeated Tuple :", Repeated_tuple)

# d) Concatenation of Tuples

Tup4 = (100,200)
Tup5 = (300,400)
Concatenated_tuple = Tup4 + Tup5
print("First Tuple :", Tup4)
print("Second Tuple :", Tup5)
print("Concatenated Tuple:", Concatenated_tuple)
