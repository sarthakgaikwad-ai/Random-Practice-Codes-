#1
class Employee():
    def __init__(self,employee_id,name,salary):
        self.employee_id = employee_id
        self.name = name
        self.salary = salary

    def category(self):
        if self.salary >= 70000:
            return "High Salary"
        elif self.salary >= 40000:
            return "Medium Salary"
        else:
            return "Low Salary"

    def display_info(self):
        print(f"Employee ID : {self.employee_id}")
        print(f"Name : {self.name}")
        print(f"Salary : {self.salary}")
        print(f"{self.category()}")

    def __str__(self):
        return (f"{self.name} has a {self.category()}")

class Company():
    def __init__(self, company_name):
        self.company_name = company_name
        self.employess = []

    def add_employee(self,Employees):
        self.employess.append(Employees)
        print(f"Added employee: {Employees.name}")

    def display_employees(self):
        print(f"Company: {self.company_name}")
        print("==========================")



e1=Employee(2001,"Sarthak",70000)

e1.display_info()
print("===================================")

e2=Employee(2002,"Shreya",40000)
e2.display_info()
print("===================================")


company= Company("Google")

company.add_employee(e1)
print(e1)

company.add_employee(e2)
print(e2)


company.display_employees()






class Applicant():
    def __init__(self,app_name,app_id,score):
        self.app_name = app_name
        self.app_id = app_id
        self.score = score
    def category(self):
        if self.score >= 80 :
            return "Merit List"
        elif self.score >= 60:
            return "Waiting List"
        else:
            return "Not Eligible"
    def display(self):
        print(f"Applicant Name is {self.app_name}")
        print(f"Applicant Id :{self.app_id}")
        print(f"Entrance Score is {self.score}")
        print(f"Catergory is {self.category()}")
class College:
    def __init__(self,college_name):
        self.college_name = college_name
        self.applicant=[]
    def add_students(self,applicant):
        self.applicant.append(applicant)
        print(f"Added applicant {applicant.app_name}")
    def display_applicant(self):
        print(f"College :{self.college_name}")
        for applicant in self.applicant:
            applicant.display()
app1=Applicant("Sarthak",2007,60)
app2=Applicant("Sakhizee",2006,85)
app3=Applicant("Princi",2006,75)
c=College("MIT ADT")
c.add_students(app1)
c.add_students(app2)
c.add_students(app3)
c.display_applicant()



class Student():
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def grade(self):
        if self.marks >= 90:
            return "Grade A"
        elif self.marks >= 75:
            return "Grade B"
        elif self.marks >= 60:
            return "Grade C"
        else:
            return "F"


class College():
    def __init__(self, college_name):
        self.college_name = college_name
        self.student = []

    def add_student(self, student):
        self.student.append(student)
        print(f"Student added {student.name}")

    def display_student(self):
        print(f"College: {self.college_name}")

        for student in self.student:
            print(f"Roll No: {student.roll_no}")
            print(f"Name: {student.name}")
            print(f"Marks: {student.marks}")
            print(f"Grade: {student.grade()}")


s1 = Student(101, "Sakhizeeool", 92)
s2 = Student(102, "principal", 78)
s3 = Student(103, "Sarthak", 65)

c1 = College("MIT ADT")

c1.add_student(s1)
c1.add_student(s2)
c1.add_student(s3)

c1.display_student()





class Book():
    def __init__(self,Book_Title,author,name,price):
        self.Book_Title = Book_Title
        self.author = author
        self.name = name
        self.price = price

    def brand(self):
        if self.price >= 1000:
            return "Premium"
        elif self.price >= 500 :
            return "Standard"
        else:
            return "Basic"

    def display_info(self):
        print(f"Book Title : {self.Book_Title}") 
        print(f"Author : {self.author}") 
        print(f"Name : {self.name}") 
        print(f"Price: {self.price}") 
        print(f"Category: {self.brand()}")

    def __str__(self):
        return (f"{self.Book_Title},wrriten by {self.author} name is {self.name} only at {self.price}")

class Library():
    def __init__(self):
        self.books=[]

    def add_book(self,book):
        self.books.append(book)
        print(f"Added book: {book.Book_Title}")


b1 = Book("The Lion King",'Lion','Jungle Book', 574)
print(b1)
b1.display_info()
print("===============================================")

b2 = Book("Data Structures", "Robert", "Brown", 750)
print(b2)
b2.display_info()
print("===============================================")

library = Library()

library.add_book(b2)


