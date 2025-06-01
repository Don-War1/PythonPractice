s1 = {20,10,50,30,100,60,90,2,80,12}
min = list(s1)[0]
max = list(s1)[len(s1)-1]
for i in s1:
    if i<min:
        min = i
    if i>max:
        max = i
print(f"Min: {min}")
print(f"Max: {max}")