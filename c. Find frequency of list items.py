def freq(l):
    D = {}
    for i in l:
        if i not in D:
            D[i] = 1
        else:
            D[i] += 1
    return D
l = input().split()
res = freq(l)
for i in res:
    print(f"{i}:{res[i]}")