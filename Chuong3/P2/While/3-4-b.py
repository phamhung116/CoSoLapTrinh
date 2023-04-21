i=1
while i<=9:
    j=1
    while j<=9-i:
        print(' ',end='')
        j+=1
    h=1
    while h<=2*i-1:
        print('*',end='')
        h+=1
    print()
    i+=1