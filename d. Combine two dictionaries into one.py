d1={"name":"Ram","email":"ram@gmail.com","mobile":8125251050}
d2={"address":"Hyderabad","gender":"Male"}
d1.update(d2)
for k,v in d1.items():
    print(f"{k}:{v}",end=" ")