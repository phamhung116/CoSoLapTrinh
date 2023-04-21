L=[]
n=int(input('n='))
for i in range(n):
    a=int(input())
    L=L+[a]
d=0
H=[]
for j in L:
    if j>0:
        d+=1
    if j%2==0:
        H=H+[j]
tong=0
for k in H:
    tong=tong+k
c=len(H)
if c==0:tbc=0
else:tbc=tong/c
print('SND=',d,sep='')
print('TBC=',tbc,sep='')