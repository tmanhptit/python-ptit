import math
n=int(input())
arr=sorted([int(x) for x in input().split()])
for i in range(n-1):
    for j in range(i+1,n):
        if math.gcd(arr[i],arr[j])==1: print(arr[i]," ",arr[j])