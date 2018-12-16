n = int(input())

for i in range(n,0,-1):
    if n%i == 1:
        n-=i
    
    if n <= 1:
        break

    
    
print(n)
