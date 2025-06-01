set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
us = set1.union(set2)
print(f"Union: {us}")
ints = set1.intersection(set2)
print(f"Intersection: {ints}")
dfs = set1.difference(set2)
print(f"Difference: {dfs}")
sdf = set1.symmetric_difference(set2)
print(f"Symmetric Difference: {sdf}")
