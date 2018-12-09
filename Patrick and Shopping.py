d1,d2,d3 = [int(i)for i in input().split()]


a1 = d1+d2+d3
a2 = (d1*2)+(d2*2)
a3 = (d1*2)+(d3*2)
a4 = (d2*2)+(d3*2)

print(min([a1,a2,a3,a4]))
