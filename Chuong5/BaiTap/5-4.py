A=[]
n=int(input('n='))
for i in range(n):
    a=int(input())
    A=A+[a]
A.reverse()
B=A
print(B)
B.sort()
print(B)