
a = list(map(int,input().split()))
people = list(map(int,input().split()))
total_group = a[0]
seat_bus = a[1]

check = 0

temp = people[0]

for i in range(0,total_group-1):
  
    if people[i] + people[i+1] <= seat_bus:
        temp = people[i] + people[i+1]
        people[i+1] = temp
        
    else:
        
        check+=1
        

print(check+1)

        
    
