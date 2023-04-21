A=[]
n=int(input('n='))
for i in range(n):
    a=int(input())
    A=A+[a]
s=0
for j in range(len(A)):
    if j%2==1 or j==1:
        s=s+A[j]
        print
print('Tong=',s,sep='')