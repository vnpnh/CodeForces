import math
a,b = [int(i) for i in input().split()]

c = int(a/b)
temp = c
d = a+c

sisa = a-(c*b)
asd = []
e = 0
for i in range(c+5):
    c+=sisa
    sisa = 0

    if c >= b:
        e = c
        
        c = int(c/b)
        
        asd.append(c)

        sisa  = e-(c*b)
    else:
        break
        
        
print(d+sum(asd))
    
        
