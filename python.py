lists=[]
while True:
    list=input("enter your items which you want:")
    if list=="":
        break
    lists.append(list)
print("shoping list--")
for i in lists:
    print(i,end=",")

