num1=float(input("enter your first number="))
num2=float(input("enter your secound number="))
op=input("enter your operator('/','*','-','+','%')=")
if(op=='+'):
    print("addition",num1+num2)
elif(op=='-'):
    print("substraction",num1-num2)
elif(op=='*'):
    print("multiplication",num1*num2)
elif(op=='/'):
    if(num2!=0):
        print("result",num1/num2)
    else:
        print("can be divisible")
elif(op=='%'):
    print("remainder",num1%num2)
else:
    print("invalid operator")
