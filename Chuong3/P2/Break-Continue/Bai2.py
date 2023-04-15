n=int(input('n='))
for i in range(1,n+1,1):
    if n%i==0 and i!=1:
        break
if i==n:print(n,'la SNT')
else:print(n,'khong la SNT')