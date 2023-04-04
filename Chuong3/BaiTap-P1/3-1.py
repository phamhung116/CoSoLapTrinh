a=float(input('a='))
b=float(input('b='))
c=float(input('c='))
p=(a+b+c)/2
import math
S=math.sqrt(p*(p-a)*(p-b)*(p-c))
S=round(S,3)
if (a+b)>c and (b+c)>a and (a+c)>b:
    print('Dien tich tam giac=',S,sep='')
else:
    print('Khong hop le')