def cheterogram(s):
    l = []
    for i in s:
        l.append(i)
        s = set(l)
    return len(l) == len(s)
s = input()
if cheterogram(s):
    print("Heterogram")
else:
    print("Not a heterogram")