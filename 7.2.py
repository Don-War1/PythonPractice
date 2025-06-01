fin=open("input.txt", "r")
fout=open("output.txt", "w")
x=1
while True:
    l=fin.readline()
    if l=="":
        break
    fout.write(str(x))
    fout.write(" ")
    fout.write(l)
    x+=1

print("Printed file successfully")
fin.close()
fout.close()