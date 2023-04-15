def Nhap():
    n=int(input('n='))
    return n
def SNT(n):
    j=2
    i=0
    while j>0:
        for e in range(1,j+1,1):
            if j%e==0 and e!=1:
                break
        if j==e:
                print(j,end='')
                i+=1
                if i<n:print(',',end='')
        if i>=n:
            break        
        j+=1
n=Nhap()
SNT(n)