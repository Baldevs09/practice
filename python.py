# n=(input())
# str=""
# i=len(n)-1
# while i>=0:
#     str+=n[i]
#     i-=1
# print(str)

## g u n j a n 5
## 0 1 2 3 4 5
# while True:
#     n = input()

#     if n.isdigit():
#         break

# print("found")

# str = "sdfsdcsdsd"
# for i in range(len(str)):
#     if str[i].isdigit():
#         print("Found")
#         break
#     else:
#         continue

# n=input()
# rev=""
# for i in range(len(n)-1,-1,-1):
#     rev+=n[i]
# if rev==n:
#     print("palindrome")
# else:
#     print("not a palindrome")

# n=input()
# count=0
# for i in range(len(n)):
#     if (n[i]=='A'or n[i]=='E' or n[i]=='I' or n[i]=='O' or n[i]=='U' or n[i]=='a'or n[i]=='e' or n[i]=='i' or n[i]=='o' or n[i]=='u'):
#         count+=1
# print(count)
# print(len(n)-count)

## aeiou -> gian

# vowel = "aeiou"
# count = 0
# n = input("Enter string")
# for i in range(len(n)):
#     if vowel.count(n[i]) > 0:
#         count+=1
# print(count)
# print(len(n)-count)

n=input()
count=0
for i in n:
    count+=1
    print("Length:",count)

