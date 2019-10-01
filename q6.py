

strvar = input("Enter string:")

length  = len(strvar)

if length < 3:
    print("unchanged string:", strvar)
elif strvar[length - 3 : length] == "ing":
    strvar = strvar + "ly"
    print("modified string:", strvar)
else:
    strvar = strvar + "ing"
    print("modified string:", strvar)





