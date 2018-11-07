n = int(input())

##a1,a2,a3 = list(map(int,input().split()))
##b1,b2,b3 = list(map(int,input().split()))
##c1,c2,c3= list(map(int,input().split()))
##

m = []
for i in range(n):
    a = list(map(int,input().split()))
    m.append(a)

##total1 = []
##check = 0
##for i in range(n):
##    check+=1
##    for j in range(n):
##        c = total[i][j]
##        total1.append(c)
##        print("aa  ",c)
#s = zip(*m) 
rez = [[m[j][i] for j in range(n)] for i in range(3)]    
d = []

##for j in range(n):
##    c = m[j][i]
##    d.append(c)
##    for i in range(n):
##        
##
check = 0

for i in range(3):
    c = sum(rez[i])
    if c == 0:
        check +=1
        
        
    




##total1 = sorted([a1,b1,c1])
##total2 = sorted([a2,b2,c2])
##total3 = sorted([a3,b3,c3])

##sums = sum(total1)
##sums2 = sum(total2)
##sums3 = sum(total3)

if check == n:
    print("YES")
else:
    print("NO")
