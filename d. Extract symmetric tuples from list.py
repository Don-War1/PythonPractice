l = [(1, 2), (2, 3), (3, 6), (3, 2), (2, 1), (8, 9)]
s1 = set(l)
s2 = set()
for i,j in l:
    t = j,i
    s2.add(t)
temp = s1.intersection(s2)
r = [(a,b) for a,b in temp if a<b]
print(r)