print("Hello THis is Calculator")
user_input=input("Enter Operation you want to Perform i.e +,-,/,x,^  :")
num1=int(input("Please Input First Number   :"))
num2=int(input("Please Input Second Number   :"))
if(user_input=="+"):
    print("Sum of ",num1,"and ",num2," is ",num1+num2)
elif(user_input=="-"):
    print("Subtraction of ",num1,"and ",num2," is ",num1-num2)
elif(user_input=="^"):
    print(num2," As Power of ",num1," is ",num1**num2)
elif(user_input=="x"):
    print("Multiplication of ",num1,"and ",num2," is ",num1*num2)
else:
    print("Division of ", num1, "/ ", num2, " is ", num1/num2)