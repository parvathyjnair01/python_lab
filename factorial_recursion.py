'''
Author:Parvathy J Nair
Description:Program to find the factorial of a number using Recursion.
'''
def factorial(n):
    if n==0:
        return 1
    else:
        return(n*factorial(n-1))
num=int(input("Enter the number:"))
factorial(num)
print("The factorial of",num,"is",factorial(num))