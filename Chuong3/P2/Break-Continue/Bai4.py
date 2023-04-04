for i in range(999999999):
    a=int(input('a='))
    b=int(input('b='))
    c=str(input('Toan tu: '))
    if c=='+':
        print(a,'+',b,'=',a+b,sep='')
    elif c=='-':
        print(a,'-',b,'=',a-b)
    elif c=='*':
        print(a,'*',b,'=',a*b)
    elif c=='/':
        print(a,'/',b,'=',a/b)
    d=str(input('Tiep tuc: '))
    if d=='t' or d=='T':
        continue
    else: 
        break