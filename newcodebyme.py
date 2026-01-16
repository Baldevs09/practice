#QUESTION 3
Customer_Id=int(input("Customer Id"))
Unit=int(input("Unit Consumed:"))
Rate=float(input("Rate per unit:"))
Total_Bill=Unit*Rate
print("Customer_Id",Customer_Id)
print("Unit Consumed:",Unit)
print("Rate per unit:",Rate)
print("Total_Bill:%.2f"%Total_Bill)
