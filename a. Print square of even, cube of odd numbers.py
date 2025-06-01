n = int(input())
even = [i**2 for i in range(1,n+1) if i%2 == 0]
odd = [i**3 for i in range(1,n+1,2)]
print(even)
print(odd)