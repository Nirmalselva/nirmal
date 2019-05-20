n=int(input())
for i in range(100):
    a=(2**i)
    if a==n:
        print("0")
        
        break
    
    elif a>n:
        x=i-1
        b=(2**x)
        c=n-b
        print(c)
        break
    else:
        continue
    
