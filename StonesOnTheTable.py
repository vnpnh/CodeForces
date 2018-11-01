a = int(input())
b = str(input())
check = 0
for i in range(len(b)-1):
    if(b[i] == b[i+1]):
        check +=1
    
print(check)
