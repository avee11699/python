mylist = ["pills", "injections", "bandage", "clips"]

while True:

    print("1. Add an item to stock pharmacy")
    print("2. Remove item from stock")
    print("3. Insert item at specified position")

    Decision = int(input("Select one point from the menu above: "))

    if (Decision == 1):
        chosen = input("Enter item name: ")
        mylist.extend([chosen])
    elif (Decision == 2):
        chosen = input("Enter item that you wish to remove: ")
        mylist.remove(chosen)
    elif (Decision == 3):
        chosen = input("insert item: ")
        position = int(input("At what position you want to insert the item"))

        if position < len(mylist):
            mylist.insert(position, chosen)
        else:
            print("invalid position")
    else:
        print("Select a valid task ")


    print(mylist)
    print("")
    print("")