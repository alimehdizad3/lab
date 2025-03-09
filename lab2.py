a=float(input())
b=float(input())
c=float(input())
x=0
while x<=1:
    if (a*x)<4:
        y=8*a*x-2*b*c
    else:
        y=9*(x**2)+3*a*b
    print("x=",x," y=",y,"\n")
    x+=0.5
