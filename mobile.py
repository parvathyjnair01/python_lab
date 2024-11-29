'''
Author:Parvathy J Nair
Description:Program to check whether the given number is a valid mobile number or not using functions.
'''
def mobile_number(number):
    number_length=len(number)
    if number_length==10:
        if number[0] in ["7","8","9"]:
            print ("valid mobile number")
        else:
            print("invalid number")
    else:
        print("invalid number")
mobile_numbers=input("Enter mobile number:")
mobile_number(mobile_numbers)