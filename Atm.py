num1=int(input("enter your first number="))
num2=int(input("enter your secound number="))
op=input("enter your op('+','-','*','/','%')=")
if(op=='+'):
    print("addition",num1+num2)
elif(op=='-'):
    print("substraction",num1-num2)
elif(op=='*'):
    print("multiplication",num1*num2)
elif(op=='/'):
    if(num2!=0):
        print("can not divisible")
    else:
        print("divisible")
elif(op=='%'):
    print("remainder",num1%num2)
else:
    print("invalid operator")
