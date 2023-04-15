a=0
b=0
for i in range(999999999999999):
    n=int(input())
    if n>0:a+=1
    elif n<0:b+=1
    elif n==0:break
    elif n!=0:continue
print(a,'so duong')
print(b,'so am')