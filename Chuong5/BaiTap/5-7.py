L=[]
n=int(input('n='))
for i in range(n):
    a=int(input())
    L=L+[a]
M=[]
for j in L:
    if j not in M:
            M.append(j)
print(M)