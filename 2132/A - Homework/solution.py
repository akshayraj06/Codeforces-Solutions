n=int(input())
for _ in range(n):
    a=int(input())
    s1=input()
    b=int(input())
    s2=input()
    s3=input()
    ans=s1
    for i in range(len(s3)):
        if s3[i]=="D":
            ans=ans+s2[i]
        else:
            ans=s2[i]+ans
    print(ans)