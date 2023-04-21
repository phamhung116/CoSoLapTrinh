A=[]
for i in range(10):
    a=int(input())
    A=A+[a]
B=[]
for j in range(0,len(A),2):
    B=B+[A[j+1]]
    B=B+[A[j]]
print(B)