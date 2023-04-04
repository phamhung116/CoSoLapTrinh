n=int(input('Nhap n:'))
i=1
while i<=n:
    j=i
    while j<i+10 and j<=n:
        print(j,end=' ')
        j=j+1
    print()
    i=i+10