d={"name":"Ram","mobile":8125251050,"gender":"Male","age":25,"address":"Hyderabad"}
kl=vl=0
for k,v in d.items():
    kl = kl + len(k)
    vl = vl + len(str(v))
print(f"Total keys length: {kl}\nTotal values length: {vl}")