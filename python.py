l = [1, 4,9,16,25,36,49,64,81,100]

i = 0
print("[", end="")

while i < len(l):
    print(l[i], end="")
    if i != len(l) - 1:
        print(", ", end="")
    i += 1

print("]")
