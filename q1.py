f1 = open("file1.txt", "w+")
f1.write('a\n')
f1.write('b\n')
f1.close()

f1 = open("file1.txt", "r")
content = f1.readlines()
f1.close()

f2 = open("file2.txt", "w+")
for x in content:
    f2.write(x)

f2.close()
