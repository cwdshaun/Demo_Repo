print("---------------------------")
print("Hello THis is Calculator")
print("---------------------------")
user_input=""
while(user_input!="Q"):
    user_input = input("Enter Operation you want to Perform i.e +,-,/,x,^,Sqrt Or Q to Quit :")
    if (user_input == "Sqrt"):
        num = int(input("Please Input The Number   :"))
        print("Square Root of ", num, "is", num ** 0.5)
    elif(user_input=="Q"):
        break
    else:
        num1 = int(input("Please Input First Number   :"))
        num2 = int(input("Please Input Second Number   :"))
        if (user_input == "+"):
            print("Sum of ", num1, "and ", num2, " is ", num1 + num2)
        elif (user_input == "-"):
            print("Subtraction of ", num1, "and ", num2, " is ", num1 - num2)
        elif (user_input == "^"):
            print(num2, " As Power of ", num1, " is ", num1 ** num2)
        elif (user_input == "x"):
            print("Multiplication of ", num1, "and ", num2, " is ", num1 * num2)
        else:
            print("Division of ", num1, "/ ", num2, " is ", num1 / num2)
print("---------------------------")
print("Thank You Very Much Bye Allah Hafiz")
print("---------------------------")