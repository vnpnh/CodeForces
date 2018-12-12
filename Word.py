a = str(input())

b = ",".join(a)
c = b.split(",")

check1 = 0 #lower
check2 = 0 #upper

for i in range(len(a)):
    if c[i].islower() == True:
        check1+=1
    else:
        check2 +=1

if check1 > check2:
    print(a.lower())
elif check1 < check2:
    print(a.upper())
else:
    print(a.lower())
    
