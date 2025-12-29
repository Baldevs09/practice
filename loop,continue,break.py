# Break and Continue Statement------
# ---------------Break Statement-------------------
i=1
while i<=5:
    print(i)
    if(i==3):
     break
    i+=1
print("end of the loop")

nums=(1,4,9,16,25,36,49,64,81,100)
x=36
i=0
while i<len(nums):
   if(nums[i]==x):
      print("found at idx",i)
      break
   else:
      print("finding")
      i+=1
print("end of loop")
# ---------------Continue Statement------------------
i = 1
while i <= 8:
    if i == 5:
        i += 1
        continue #skip
    print(i)
    i += 1

i=1
while i<=10:
    if(i%2!=0):
        i+=1
        continue
    print(i)
    i+=1

# -----------------For loop-------------------
nums=[21,56,5,86,53]
for x in nums:
    print(x)

tup=(12,56,8,94,56)
for x in tup:
    print(x)

str="baldev singh jaat"
for x in str:
    print(x)
else:
    print("End of str")

str="baldev singh jaat"
for x in str:
    if(x=='i'):
        print("i found")
        break
    print(x)
else:
    print ("End of str")
