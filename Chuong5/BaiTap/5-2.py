def Input():
    L=[]
    n=int(input('n='))
    i=0
    while i<n:
        a=int(input())
        L=L+[a]
        i+=1
    return L
def Search(L):
    max=L[0]
    min=L[0]
    for j in L:
        if j>max:max=j
        if j<min:min=j
    return max,min
def Output(max,min):
    print(max,min)
L=Input()
max,min=Search(L)
Output(max,min)