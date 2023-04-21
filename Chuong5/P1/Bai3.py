x=int(input('x='))
k=int(input('k='))
L=[]
n=int(input('n='))
for i in range(n):
    a=int(input())
    L=L+[a]
def delete(L,x):
    while x in L:
        L.remove(x)
    print(L)
delete(L,x)