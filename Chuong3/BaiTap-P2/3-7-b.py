for i in range(1,99999999999,1):
    n=int(input())
    s=1
    for j in range(1,n+1,1):
        s=s*j
    if n>=0:print(s)
    if n<0:break
    else:continue