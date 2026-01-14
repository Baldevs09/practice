#QUESTION=1
Roll_Number=int(input("Roll Number:"))
Mathematices=int(input("Mathematices:"))
Science=int(input("Science:"))
English=int(input("English"))
Total_marks=Mathematices+Science+English


print("Roll Number:",Roll_Number)
print("Mathematices:",Mathematices)
print("Science:",Science)
print("English:",English)
print("Total Marks:",Total_marks)
print("Average_marks:%.2f"%((Mathematices+Science+English)/3))
print("Student Identifier:",Roll_Number)
