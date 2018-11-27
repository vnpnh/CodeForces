n = int(input())

b = []
temp = 0
temp2 = 0

for i in range(n):
    a = list(map(int,input().split()))
    temp = abs(temp-a[0])
    temp2 = abs(temp+a[1])
    temp = temp2
    b.append(temp)
    
print(max(b))
    
