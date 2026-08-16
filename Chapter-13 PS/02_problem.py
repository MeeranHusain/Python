# 2. Write a program to input name, marks and phone number of a student and format it using the format function like below

name = input("Enter the name of the student: ")
marks = float(input("Enter the marks of the student: "))
phone_number = input("Enter the phone number of the student: ")

formatted_output = "Student Name: {}\nMarks: {:.2f}\nPhone Number: {}".format(name, marks, phone_number)

print(formatted_output)