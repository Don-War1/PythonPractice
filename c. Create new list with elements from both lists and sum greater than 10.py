a = list(map(int,input().split()))
b = list(map(int,input().split()))
r = [x+y for x,y in zip(a,b) if x+y>10]
print(r)