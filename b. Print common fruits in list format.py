l1 = ["apple", "banana", "cherry", "kiwi", "mango","Papaya"]
l2 = ["aPPLe", "BaNaNa", "ORANGE", "KiWi", "manGO","Grape"]
l = []
for i in l1:
    for j in l2:
        f1 = i.casefold()
        f2 = j.casefold()
        if f1 == f2:
           l.append(i)
print(l)
#alternative process
l1 = ["apple", "banana", "cherry", "kiwi", "mango","Papaya"]
l2 = ["aPPLe", "BaNaNa", "ORANGE", "KiWi", "manGO","Grape"]
l = []
for i in l1:
    for j in l2:
        if i == j.lower():
           l.append(i)
print(l)