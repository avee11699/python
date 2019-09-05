num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))

if num1 > num2:
    smaller = num2
else:
    smaller = num1

for i in range(1, smaller + 1):
    if ((num1%i == 0) and (num2%i == 0)):
        hcf = i
        print("The H.C.F of the first number", num1, "and the second number", num2, "is", hcf)
