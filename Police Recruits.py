n = int(input())

t = [int(i)for i in input().split()]

police = 0
crime = 0
unt = 0
for i in range(n):
    
    if t[i] >= 1:
        
        police+=t[i]
       

    if t[i] == -1:
        police -=1
    
    if police < 0 :
        
        crime+=1
        police = 0
   
print(crime)
