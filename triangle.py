'''
Author:Parvathy J Nair
Description:A program that accepts the lengths of three sides of a triangle as inputs.
The program should output whether or not the triangle is a right triangle.
 Implement using functions.
 '''
def right_triangle():
    a=int(input("Enter hypotenuse side:"))
    b=int(input("Enter base side:"))
    c=int(input("Enter altitude side:"))
    if a*a==b*b+c*c:
        print ("Right angled triangle")
    else:
        print("Not right angled")
right_triangle() 