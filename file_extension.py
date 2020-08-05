f = input("enetr: ")
x = 0
for i in range(len(f)):
    if f[i] == ".":
        x = i
print("the filename is: ", f)
print("the extension of the file is: ", f[x+1: ])

