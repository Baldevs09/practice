Balance=float(input("enter your amount="))
Atm=float(input("enter your amount="))
if(Atm<=0):
    print("invalid amount")
elif(Balance-Atm<=1000):
    print("minmum amount")
elif(Balance>Atm):
    print("valid amount")
else:
    print("withdrwal sucessfully")
    print("remaining amount",Balance-Atm)

