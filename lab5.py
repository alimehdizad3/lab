n=10
hasil=1
a=[0]*n
from random import randint
for i in range(n):
    a[i]=randint(4,47)
for i in a:
    if i%3==1:
        hasil*=i
print(hasil)
