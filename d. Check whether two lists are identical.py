def checkid(l1,l2):
    flag = True
    if len(l1) != len(l2):
        return False
    else:
        for i in range(0,len(l1)):
            if l1[i] != l2[i]:
                return False
    return flag

l1 = list(map(int,input().split()))
l2 = list(map(int,input().split()))
if checkid(l1,l2):
    print("Identical Lists")
else:
    print("Not identical lists")