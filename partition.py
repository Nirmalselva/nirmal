print("enter the value")
n,a,b=map(int,input().split())
if n%2==0:
    if a+b==n:
        print("yes")
    elif a+b>n:
        print("no")
    elif a%2==0 and b%2==0:
        print("no")
    else:
        print("yes")
else:
    if a+b==n:
        print("yes")
    elif a+b<n:
        print("no")
    else:
        print("no")
    
