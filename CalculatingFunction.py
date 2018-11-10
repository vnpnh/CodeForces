import math
n = int(input())
a = n/2
temp = 0
if n%2 == 0:
    print(math.ceil(a))
else:
    temp = math.ceil(a)
    print(-temp)
