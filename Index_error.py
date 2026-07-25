numbers = []

try:
    n = int(input("How many elements do you want to add? "))

    for i in range(n):
        value = int(input(f"Enter element {i+1}: "))
        numbers.append(value)

    print("Your list:", numbers)

    index = int(input("Enter index to access: "))
    print("Element at index:", numbers[index])

except ValueError:
    print("ValueError: Please enter only integers.")

except IndexError:
    print("IndexError: Index out of range.")

    # output
# How many elements do you want to add? 2
# Enter element 1: 1
# Enter element 2: 2
# Your list: [1, 2]
