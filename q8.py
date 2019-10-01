
longest = 0

while True:

    word = input("Enter word: ")
    length = len(word)
    if length > longest:
        longest = length

    print("choose 1 to continue to enter word, 2 to exit")
    choice = int(input("Enter choice: "))
    if choice == 2:
        break
    elif choice == 1:
        print()
    else:
        print("Invalid choice!")


print("Longest length:", length)





