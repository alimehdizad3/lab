n=int(input())
m=int(input())
a=[]
for i in range(n):
    setir=[]
    for i in range(m):
        element=int(input())
        setir.append(element)
    a.append(setir)
print(a)
for i in range(n):
    cem=0
    for j in range(m):
        cem+=a[i][j]
    if cem<0:
        print(i+1)
