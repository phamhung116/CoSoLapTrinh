i=1
while i<=9:
    j=1
    while j<=9-i:
        print(' ',end='')
        j+=1
    j=1
    while j<=2*i-1:
        print('*',end='')
        j+=1
    print()
    i+=1