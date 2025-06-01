d={"Chandhu":99,"Eesha":74,"Dhanush":86,"Fanindra":67,"Bharath":44,"Abhi":56}
l=[]
for k in d.keys():
    l.append(k)
for i in range(0,len(l)):
    for j in range(0,len(l)):
        if l[i]<l[j]:
            l[i],l[j] = l[j],l[i]
print("Sorted Names")
for k in l:
    print(f"{k}:{d.get(k)}",end=" ")