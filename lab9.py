import math
a, b = 2.6, 3
e=0.0001
x0=((math.e)**(4*a)+5.5)**(1/3)
x=((math.e)**(4*x0)+5.5)**(1/3)
while abs(x-x0)>e:
    x0=round(x, 4)
    x=((math.e)**(4*x0)+5.5)**(1/3)
    x=round(x, 4)
print(round(x, 4))
