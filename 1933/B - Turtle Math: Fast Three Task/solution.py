t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    summ=0
    for i in range(n):
        summ+=arr[i]
    if summ%3==0:
        print(0)
    elif summ%3==1:
        if 1 in [x%3 for x in arr]:
            print(1)
        else:
            print(2)
    else:
        print(1)