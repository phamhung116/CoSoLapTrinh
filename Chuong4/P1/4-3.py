def Nhap():
    a=float(input('a='))
    b=float(input('b='))
    toantu=str(input('Toan tu: '))
    return a,b,toantu
def Tinh(a,b,toantu):
    if toantu=='+':
        s=a+b
    elif toantu=='-':
        s=a-b
    elif toantu=='*':
        s=a*b
    elif toantu=='/':
        s=a/b
    return s
def kq(a,toantu,b,s):
    print(a,toantu,b,'=',s,sep='')
i=1
while i>0:
    a,b,toantu=Nhap()
    s=Tinh(a,b,toantu)
    kq(a,toantu,b,s)
    tieptuc=str(input('Tiep tuc: '))
    if tieptuc=='t' or tieptuc=='T':
        break
    else: continue