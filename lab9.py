import math
x0, e = 2.6, 3.0
x=(x0+1)**(1/3)
while abs(x-x0)>e:
    x=(x0+1)**(1/3)
    x0=x
    print(x)
print(round(x, 4))
