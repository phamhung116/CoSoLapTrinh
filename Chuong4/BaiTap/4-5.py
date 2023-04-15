def LaSoNguyenTo(x):
    if x<2:
        return False
    for i in range(2,x+1,1):
        if x%i==0:
            break
    if x==i:
        return True
def SoHopLe(x):
    return x<=1
def NhapVaDem():
    j=1
    kq=0
    while j>0:
        x=int(input())
        if LaSoNguyenTo(x):kq+=1
        if SoHopLe(x):break
    return kq
def InKQ(kq):
    print('Co',kq,'so nguyen to')
print('Nhap day so:')
kq=NhapVaDem()
InKQ(kq)