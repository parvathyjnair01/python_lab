while True:
    print("\n1.Convert Celsius to Fahrenheit")
    print("2.Convert Fahrenheit to Celsius")
    print("3.Exit the program")
    option=int(input("Enter your option:"))
    if option==1:
      temp=int(input("Enter temperature in celsius:"))
      fahrenheit = (temp * 9 / 5) + 32
      print(f"fahrenheit: {fahrenheit}")
    elif option==2:
        temp=int(input("Enter temperature in fahrenheit:"))
        celsius = (temp - 32) * 5 / 9
        print(f"celsius: {celsius}")
    elif option==3:
        break
    else:
        print("Invalid option")




