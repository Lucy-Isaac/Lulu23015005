num1=int(input("Enter a number: "))

print("Multiplication table for:", )
for i in range (num1, 13):
    for j in range (1, 13):
        print(i, "x", j, "= ", i*j)