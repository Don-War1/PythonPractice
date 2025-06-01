l = list(map(int,input().split()))
min = l[0]
max = l[len(l)-1]
for i in l:
    if i<min:
        min = i
    if i>max:
        max = i
print(f"Min: {min}")
print(f"Max: {max}")