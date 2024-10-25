
var=int(input("Enter temperature:"))
scale=input("Is this in (C)elsius or (F)ahrenheit? ")
f=(9/5*var)+32
if scale=="c":
    print(var,"celcius is",f, "fahrenheit" )
else:
    c=5/9*(var-32)
    print(var,"fahrenheit is",c,"celcius")
