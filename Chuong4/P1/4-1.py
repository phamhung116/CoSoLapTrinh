def Nhap():
    n=int(input('n='))
    return n
def SNT(n):
    for i in range(1,n+1,1):
        if n%i==0 and i!=1:
            break
    a=i
    return a
def KQ(a):
    if a==n:print(n,'la SNT')
    else:print(n,'khong la SNT')
n=Nhap()
a=SNT(n)
c=KQ(a)