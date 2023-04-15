import math
def nhap():
    a=int(input('a='))
    b=int(input('b='))
    c=int(input('c='))
    return a,b,c
def giaipt(a,b,c):
    if (b*b-4*a*c)==0:
        x=-b/(2*a)
        print('Phuong trinh co nghiem kep')
        print('x1=x2=',x,sep='')
    elif (b*b-4*a*c)>0:
        x1=(-b+math.sqrt(b*b-4*a*c))/(2*a)
        x2=(-b-math.sqrt(b*b-4*a*c))/(2*a)
        print('Phuong trinh co hai nghiem')
        inkq(x1,x2)
    elif (b*b-4*a*c)<0:
        print('Phuong trinh vo nghiem')
    return x1,x2
def inkq(x1,x2):
    print('x1=',x1,sep='')
    print('x2=',x2,sep='')
a,b,c=nhap()
giaipt(a,b,c)