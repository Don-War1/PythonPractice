def arithoper(a,b):
    add = a + b
    sub = a - b
    mul = a * b
    div = a / b
    return add, sub, mul, div

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    a, s, m, d = arithoper(x, y)
    print(a,s,m,d,sep="\n")
