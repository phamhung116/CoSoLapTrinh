a=str(input())
b=int(input())
for i in range(1,b+1,1):
    for j in range(1,b+1,1):
        if j<=i:
            print(a,end=' ')
    print()