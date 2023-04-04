a=float(input())
b=float(input())
c=float(input())
if (a+b)>c and (b+c)>a and (a+c)>b:
    if a==b==c:print('Tam giac deu')
    elif a*a==b*b+c*c or b*b==c*c+a*a or c*c==b*b+a*a:print('Tam giac vuong')
    else:print('Tam giac khac')
else:print('Khong hop le')