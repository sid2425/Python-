operand1=int(input("Enter the value of operand 1:"))
operand2=int(input("Enter the value of operand 2:"))
print("-------------------------")
print("1-Add 2-Sub 3-Multiply 4-Divsion")
choice=input("Enter the choice")
if choice=="1":
    result=operand1+operand2
    print("Hence the result is",result)
elif choice=="2":
    result=operand1-operand2
    print("Hence the result is",result)
elif choice=="3":
    result=operand1*operand2
    print("Hence the result is",result)
elif choice=="4":
    result=operand1/operand2
    print("Hence the result is",result)
else: 
    print("OOPS! You have entered an invalid operation please enter valid choice")
    print("1-Add 2-Sub 3-Multiply 4-Divsion")
