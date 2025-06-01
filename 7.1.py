fin=open("input.txt", "r")
fout=open("output.txt", "w")
while True:
    l=fin.readline()
    fout.write(l)
    if l=="":
        break
print("Copied file successfully")
fin.close()
fout.close()