'''Author:Parvathy J Nair
DEscription:Recursive function to multiply two positive numbers'''
def recursive_mul(num1,num2):
    if num2==1:
        return num1
    else:
        return num1+recursive_mul(num1,num2-1)
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
result=recursive_mul(num1,num2)
print("The muliplication of two numbers is:",result)