n=int(input('n='))
S=1
for i in range(1,n+1,1):
    S=S*i
print(n,'!=',sep='',end='')
print(S)