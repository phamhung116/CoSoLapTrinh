def nhap():
    n=int(input('n='))
    return n
def inkq(n):
    for i in range(2,n+1,2):
        print(i,end=' ')
j=1
while j>0:
    n=nhap()
    inkq(n)
    print()
    a=str(input('Tiep tuc khong?'))
    if a=='k' or a=='K':
        break
    else:continue