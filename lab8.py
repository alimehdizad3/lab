import math
a,b = 2.6, 3.0
e = 0.01
while (b-a)>e:
    x=(a+b)/2
    if (((x**3)-(math.e)**(4*x)-5.5)*((b**3)-(math.e)**(4*b)-5.5))<0:
        a=x
    else:
        b=x
print(x)
