import random
lst = [ ]
for i in range(10):
    number = random.randint(0, 101) 
    lst = lst + [number]
print("lst = ", lst)
f = open('file.txt', 'w')
s=str(len(lst))
f.write(s + '\n')
for i in lst:
    s = str(i) 
    f.write(s + ' ')
f.close()
f=open('file.txt','r')
s=f.readline()
lst2=[ ]
for line in f:
    strs=line.split()
    print('strs=',strs)
    for s in strs:
        if s!='':
            lst2=lst2+[int(s)]
print('lst2=',lst2)
b=[ ]
f1 = open('file1.txt', 'w')
for x in lst2:
    if x%3==0:
        b.append(x)
print('4-e bolunen ededler:',b)
s=str(len(b))

f1.write('3-e bolunen edeler: ')
for i in b:
    s=str(i)
    f1.write(s + ' ')
total=0
for i in b:
    total+=int(i)
f1.write('\n' + '3-e bolunen edelerin cemi: ' + str(total))
print('3-e bolunen ededlerin cemi:', total)
f.close()
f1.close()
