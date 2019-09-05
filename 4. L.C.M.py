num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number:"))
if(num1 > num2):
    min1 = num1
else:
    min1 = num2
while(2):
    if(min1%num1 == 0 and min1%num2 == 0):
        print("The L.C.M of the first number", num1, "and the second number", num2, "is", min1)
        break
    min1 += 1
