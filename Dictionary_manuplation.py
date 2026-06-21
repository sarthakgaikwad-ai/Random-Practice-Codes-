"""
Write a Python program to perform following operations on Dictionaries :
a) Create and access dictionary elements
b) Update Dictionary
c) Removing elements
d) Merging dictionaries
"""

# a) Create and access dictionary elements

Student = {
    "Name": "Sarthak",
    "Roll_no": 22,
    "Branch": "CSE",
    "Marks": 90
}

print("Dictionary Elements :", Student)

print("Accessing Elements:")
print("Name:", Student["Name"])
print("Marks:", Student["Marks"])


# b) Update Dictionary

Student["Marks"] = 90          # Update existing value
Student["Year"] = "Second"     # Add new key-value pair

print("After Updating Dictionary :", Student)

# c) Removing elements

Student.pop("Roll_no")         # Remove specific element
del Student["Branch"]        # Another way to remove element

print("After Removing Elements :", Student)


# d) Merging dictionaries

Extra_info = {
    "College": "MIT ADT",
    "City": "Pune"
}

Merged_dict = Student | Extra_info  

print("After Merging Dictionaries :", Merged_dict)
