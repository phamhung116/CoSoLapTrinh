x=float(input('x='))
y=float(input('y='))
ch=str(input('Phep toan:'))
if ch=='+':
    a=x+y
    a=round(a,1)
    print(x,ch,y,'=',a,sep='')
elif ch=='-':
    a=x-y
    a=round(a,1)
    print(x,ch,y,'=',a,sep='')
elif ch=='*':
    a=x*y
    a=round(a,1)
    print(x,ch,y,'=',a,sep='')
elif ch=='/' and y==0:
    print('Khong hop le')
elif ch=='/':
    a=x/y
    a=round(a,1)
    print(x,ch,y,'=',a,sep='')
else:
    print('Khong hop le')