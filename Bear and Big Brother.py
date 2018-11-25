a = list(map(int,input().split()))
limak = a[0]
bob = a[1] #his brother
#limak weight is tripled after every year,
#while Bob's weight is doubled after every year.

total = 0
bet = abs(bob-limak)

if limak == bob:
        total = 1

if total == 0:
    for i in range(bet+1):
        
        if limak > bob:
            break
        limak*=3
        bob *= 2
        total+=1
    

print(total)
    
    
