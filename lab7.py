import random

lst1 = []
for i in range(10):
    number = random.randint(0, 101)
    lst1.append(number)

print("lst1 = ", lst1)

with open('lab7_1.txt', 'w') as f:
    s = str(len(lst1))
    f.write(s + '\n')  
    for i in lst1:
        s = str(i)
        f.write(s + ' ')

with open('lab7_1.txt', 'r') as f:
    s = f.readline()  
    lst2 = []
    for line in f:
        strs = line.split() 
        for s in strs:
            if s != '':
                lst2.append(int(s))  

print('lst2 = ', lst2)

b = [x for x in lst2 if x % 3 == 0]
print('3-e bolunen ededler:', b)

sum_b = sum(b)
print('3-e bolunen ededlerin cemi:', sum_b)

with open('lab7_2.txt', 'w') as f:
    f.write(f"3-e bolunen edeler: {b}\n")
    f.write(f"Cem: {sum_b}\n")
    for i in b:
        f.write(str(i) + ' ')
