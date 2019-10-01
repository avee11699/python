
text = input("Enter a text")

pos_not = text.find('not')
pos_poor = text.find('poor')

if pos_not != -1 and pos_poor != -1:
    text = text[0:pos_not] + 'good' + text[pos_poor + 4:]
    print(text)
else:
    print("Not Found")






