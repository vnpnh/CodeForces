import math
a = list(map(int,input().strip().split()))
m = a[0]
n = a[1]
s = a[2]

total = math.ceil(m/s)*math.ceil(n/s)
        
    
print(total)


