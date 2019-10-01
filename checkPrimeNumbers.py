
def checkfactor(num):
    for i in range(2, num):
        if (num % i) == 0:
            return "This is not a Prime Number"
        else:
            return "This is a prime number"


number = int(input("Enter number: "))

if number <= 1:
    msg = "This is not a prime Number!"
else:
    if number != 2:
        msg = checkfactor(number)
    else:
        msg = "This is a prime number"



print(msg)




