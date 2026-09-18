# Movie Ticket Pricing : Movie tickets are based on age $12 for adults(18 and oveer ,$8 for children.Eveyone gets a $2 discont on wed 
age=int(input("Enter your age : "))
day=input("What is the day")
price = 12 if age>=18 else 8
if day == "Wednesday":
    price = price - 2
print(f"The Ticket price is : {price}")

# Fruit ripness checker : check ripness of fruit on colour 
fruit="Bannana"
colour="Yellow"

if fruit == "Bannana":
    if colour == "Green":
        print("Unripe")
    elif colour == "Yellow":
        print("Ripe")
    elif colour == "Brown":
        print("Overripe")

# Weather Activity Suggestion 
weather = "Sunny"

if weather == "Sunny":
    activity = "Go for walk"
elif weather == "Rainy":
    activity = "Sleep in the home"
elif weather == "Snowy":
    activity = " make a snow man"
print("You shoul {activity}")


#Passwrd checker
password = input("Enter you pass")
password_len = len(password)

if password_len < 6 :
    strength = "Weak"
elif password_len<= 10:
    strength = "Medium"
else:
    strength = "Strong"

print("Password strength is : ",strength)

