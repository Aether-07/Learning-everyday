
#problem 1
total = 0
l1 = []
for i in range(0,1000):
    if i%3==0:
        l1.append(i)
    elif i%5==0:
        l1.append(i)
    else:
        pass
print(l1)
for n in l1:
    total = total + n

print(total)

#login test for project eular
x = 0
total1 = 0
lst1 = []
for i in range(0,820001):
    x = i*i
    lst1.append(x)
for n in lst1:
    if n%2==0:
        pass
    else:
        total1 = total1+n
print(total1)

#problem 2 (fibonacci)
a = 0
b = 1
sumi = 0
lp = []
lppp=[]

while a<=4000000:
    lp.append(a)
    next_num = a+b
    a = b
    b = next_num

for k in lp:
    if k%2==0:
        lppp.append(k)
    else:
        pass
for h in lppp:
    sumi = sumi +h

print(lp)
print(sumi)