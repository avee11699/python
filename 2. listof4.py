list1 = []
list2 = []
list3 = []
list4 = []

decision = "yes"
while decision != "no":
    sum1=0
    for i in range(4):
        list1.append(input("Enter numbers in list 1:"))
        sum1 = sum1 + int(list1[i])
    print("")
    sum2 = 0
    for i in range(4):
        list2.append(input("Enter numbers in list 2:"))
        sum2 = sum2 + int(list2[i])
    print("")
    sum3 = 0
    for i in range(4):
        list3.append(input("Enter numbers the list 3:"))
        sum3 = sum3 + int(list3[i])
    print("")
    sum4 = 0
    for i in range(4):
        list4.append(input("Enter numbers in list 4:"))
        sum4 = sum4 + int(list4[i])
    print("")

    if (sum1 > sum2) and (sum1 > sum3) and (sum1 > sum4):
        print("The First list",list1, "has the highest sum of",sum1)
    elif (sum2 > sum1) and (sum2 > sum3) and (sum2 > sum4):
        print("The Second list",list2, "has the highest sum of",sum2)
    elif (sum3 > sum1) and (sum3 > sum2) and (sum3 > sum4):
        print("The Third list",list3, "has the highest sum of",sum3)
    else:
        print("The Fourth list",list4, "has the highest sum of",sum4)

    decision = input("would you retry the program?(yes/no): ")
