x=int(input('x='))
k=int(input('k='))
L=[]
n=int(input('n='))
for i in range(n):
    a=int(input())
    L=L+[a]
def search(L,x):
    if x in L:
        b=L.index(x)
        print(b)
        return b
    else: 
        return None
search(L,x)