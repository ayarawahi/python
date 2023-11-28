file = open("test.txt.txt", "r")

for i in file:
    i=i.split(" ")
    if int(i[1]) >20:
        print(i[0],"mark is ",i[1])
#file.write("Hello, World!\n")
#ile.close()