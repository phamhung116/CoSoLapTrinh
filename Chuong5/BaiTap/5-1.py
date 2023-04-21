def Input():
    L=[]
    n=int(input('n='))
    i=0
    while i<n:
        a=int(input())
        L=L+[a]
        i+=1
    x=int(input('x='))
    return L,x
def FirstAndLast(L):
    L1=[L[0],L[-1]]
    print(L1)
def Search(L,x):
    if x in L:
        print('True')
        return True
    else: 
        print('False')
        return False
L,x=Input()
FirstAndLast(L)
Search(L,x)