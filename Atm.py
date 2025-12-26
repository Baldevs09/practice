Balance=float(input(" enter the amount"))
Atm=float(input("emter the amount"))

if(Atm<=0):
    print("invalid amount")
elif(Atm>Balance):
    print("amount is valid",Atm)
elif(Balance-Atm)<1000:
    print("amount is minimum")
else:
    print("withdrawel sucessfully")
    print("remaing amount",Balance-Atm)
