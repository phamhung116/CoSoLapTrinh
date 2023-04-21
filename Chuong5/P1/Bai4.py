x=int(input('x='))
k=int(input('k='))
L=[]
n=int(input('n='))
for i in range(n):
    a=int(input())
    L=L+[a]
def count(L):
    print(len(L))
count(L)