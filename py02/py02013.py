
while True:
    n=int(input())
    if n==0: break

    dem=0
    while n!=1:
        dem+=1
        if n%2==0: n/=2
        else: n=n*3+1
    if dem==0: print(1)
    else: print(dem+1)