fin = open("input.txt","r")
while True:
    line = fin.readline()
    if line == "":
        break
    print(line,end = "")
fin.close()
print("\n\nFile read successfully.")
