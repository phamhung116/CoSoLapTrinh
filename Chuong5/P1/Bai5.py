x=int(input('x='))
k=int(input('k='))
L=[]
n=int(input('n='))
for i in range(n):
    a=int(input())
    L=L+[a]
y='y'
def replace(L,x,y):
    if x in L:
        j=L.index(x)
        L.insert(j,y)
        L.remove(x)
    print(L)
replace(L,x,y)