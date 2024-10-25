"""Author:Parvathy J Nair
Date:25-10-2024
Description: Python program to find the largest of three numbers.
The program should take three numbers as input from the user
and determine which one is the largest.
 Use conditional statements to compare the numbers"""
num1=int(input("Enter First number:"))
num2=int(input("Enter Second number"))
num3=int(input("Enter Third number:"))
if num3>num1 and num3>num2:
    print("The largest number is:",num3)
elif num1>num2:
    print(num1,"is greaterthan num2")
else:
    print(num2,"is greater")