e=0.01
x=0.1
i=1
y=0
a=0
b=-1
while abs((x**i)/i)>e:
  a=-b*((x**i)/i)
  y+=a
  i+=1
print(y)
