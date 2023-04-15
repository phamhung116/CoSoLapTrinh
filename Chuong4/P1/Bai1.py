def Nhap():
    n=int(input('n='))
    return n
def NhapVaDem(n):
    c=0
    i=1
    print('Nhap',n,'so nguyen:')
    while i<=n:
        a=int(input())
        if a%2==0:c+=1
        i+=1
    return c
def InKQ(c):
    print("So chu so chan la:",c)
n=Nhap()
c=NhapVaDem(n)
d=InKQ(c)