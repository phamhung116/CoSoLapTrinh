x=int(input('x='))
k=int(input('k='))
L=[]
n=int(input('n='))
for i in range(n):
    a=int(input())
    L=L+[a]
def add(L,x,k):
    if k>len(L):
        L.append(x)
    else:L.insert(k,x)
    print(L)
add(L,x,k)