d = {'a':'Apple','b':'Ball','c':'Cat','d':'Dog','E':'Elephant'}
s = "-"
print(f"{s*5}Keys{s*5}")
for i in d.keys():
    print(i,sep=" ",end=" ")
print(f"\n{s*5}Values{s*5}")
for i in d.values():
    print(i,sep=" ",end=" ")
print(f"\n{s*5}Key and Values{s*5}")
for i in d.items():
    print(f"{i[0]}:{i[1]}",sep=" ",end=" ")