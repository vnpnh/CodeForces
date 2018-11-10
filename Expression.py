a = int(input())
b = int(input())
c = int(input())

t1 = a+b*c
t2 = a*(b+c)
t3 = a*b*c
t4 = (a+b)*c
t5 = a+b+c
t6 = (abs(a)+abs(b))*abs(c)
t7 = abs(a)+(abs(b)*abs(c))


temp = [t1,t2,t3,t4,t5,t6,t7]
print(max(temp))













