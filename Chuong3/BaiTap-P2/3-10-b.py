n=int(input('n='))
for i in range(1,n+1,5):
    for j in range(i,n+1,1):
        if j<i+5:
            print(j,end=' ')
    print()