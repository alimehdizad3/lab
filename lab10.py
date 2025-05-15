import math
a, b, e= 2.6, 3, 0.001
x0=a
t=(x0**3-math.e**(4*x0)-5.5)/(3*(x0**2)-4*(math.e)**(4*x0))
while abs(t)>e:
    x0=x0-t
    t=(x0**3-math.e**(4*x0)-5.5)/(3*(x0**2)-4*(math.e)**(4*x0))
print(x0)
