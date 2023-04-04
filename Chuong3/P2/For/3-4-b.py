for i in range(1,10,1):
    for j in range(1,9-i+1,1):
        print(' ',end='')
    for j in range(1,2*i,1):
        print('*',end='')
    print()