n=int(input('n='))
for i in range(1,n+1,10):
    for j in range(i,n+1,1):
        if j<i+10:
            print(j,end=' ')
    print()