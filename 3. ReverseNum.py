number=int(input("Enter a number:"))
original = number
reverse=0
similar = "False"
while(number > 0 and similar != "True"):

    reverse = reverse*10+ number %10
    number = number//10
if(original == reverse):
    similar = "True"
    print("The reverse number is the same as the original number?",similar)
else:
    print(similar)
    print("The reverse number is not the same as the original number")
    print("Try another number!")