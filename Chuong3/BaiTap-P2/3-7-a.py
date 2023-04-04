i=1
while i>0:
    n=int(input())
    s=1
    j=1
    while j<=n and j>0:
        s=s*j
        j+=1
    
    if n<0:break
    else:
        print(s)
        continue