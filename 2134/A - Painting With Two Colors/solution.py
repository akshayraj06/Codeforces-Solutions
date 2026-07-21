t=int(input())
for i in range(t):
    n,a,b=map(int,input().split(" "))
    if (n-b)%2!=0:
        print("No")
    elif a<=b:
        print("Yes")
    elif (n-a)%2==0:
        print("Yes")
    else:
        print("NO")