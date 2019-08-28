upper = 0
lower = 0
digit = 0
specialChar = 0

word = input("Enter your sentence: ")

for i in word:
    if i.isalpha() and i.isupper():
        upper += 1
    elif i.isalpha() and i.islower():
        lower += 1
    elif i.isnumeric():
        digit += 1
    else:
        specialChar += 1

print("Total Number of Uppercase letter in the sentence = ", upper)
print("Total Number of Lowercase letter in the sentence = ", lower)
print("Total Number of Digits in the sentence is ", digit)
print("Total Number of special character in the sentence is", specialChar)