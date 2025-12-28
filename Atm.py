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
n=int(input("enter your table number="))6
i=1
while i<=10:
    print(n*i)
    i+=1
nums=[1,4,9,16,25,36,49,64,81,100]
index=0
while index<len(nums):
    print(nums[index])
    index += 1
heroes=["ironman","doctorstrange","mike","lucus"]
idx=0
while idx<len(heroes):
    print(heroes[idx])
    idx+=1
nums=(1,4,9,16,25,36,49,64,81,100)
x=36
i=0
while i<len(nums):
    if(nums[i]==x):
        print("FOUND",i)
    i+=1
