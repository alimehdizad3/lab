import math
l1= math.sqrt((2.591*(0.836)**(1/3))/(1.147*(math.e**2+math.e**(-2))))
l2=(-math.log10(0.8)**(1/3))*math.tan(4)
if abs(l1)< 1+abs(l2):
    u=(3*l1-5*l2)/(l1**2+l2**2)
elif abs(l1)>=1+abs(l2):
    u=(3*l1+5*l2)/(l1**2-l2**2)
print(u)
