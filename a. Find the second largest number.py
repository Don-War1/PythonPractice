l = list(map(int,input().split()))
sl = []
for i in l:
    if i not in sl:
        sl.append(i)
for i in range(0,len(sl)):
    for j in range(0,len(sl)):
        if sl[i]<sl[j]:
            sl[i],sl[j] = sl[j],sl[i]
print(sl[-2])