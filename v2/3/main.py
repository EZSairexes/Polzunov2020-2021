from itertools import *

n = int(input())
print(10)
for i in permutations('0123456789', n):
    k = i
    for j in range(len(k)):
        print(k[j], end=' ')
print()

