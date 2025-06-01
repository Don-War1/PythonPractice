fin=open("input.txt","r")
l1=[]
line=word=character=0
while True:
    l=fin.readline()
    if l=="":
        break
    line+=1
    l1=l.split()
    for w in l1:
        word+=1
        character+=len(w)
print(f"No. of lines={line}")
print(f"No. of words={word}")
print(f"No. of characters={character}")

