def checkdisj(set1,set2):
    ctr = 0
    for x in set1:
        if x in set2:
            ctr += 1
    if ctr>0:
        return False
    else:
        return True
l1 = set(input().split(" "))
l2 = set(input().split(" "))
s1 = set()
s2 = set()
for i in l1:
    s1.add(i)
for i in l2:
    s2.add(i)
if checkdisj(s1,s2):
    print("Disjoint")
else:
    print("Not disjoint")