fin=open("input.txt","r")
l1=[]
l2=[]
while True:
    l=fin.read()
    if l=="":
        break
    l=l.lower()
    l1=l.split()
    for w in l1:
        for i in w:
            if (i not in l2) and (i!=" "):
                l2.append(i)
    for i in range(0,len(l2)):
        for j in range(0,len(l2)):
            if l2[i]<l2[j]:
                l2[i],l2[j]=l2[j],l2[i]
    for i in l2:
        print(i,end=" ")


