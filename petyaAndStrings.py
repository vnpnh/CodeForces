a = str(input()).lower()
b = str(input()).lower()

check1 = 0 
for i in range(len(a)):
    if ord(a[i]) > ord(b[i]):
        check1 = 1
        
        
    if ord(a[i]) < ord(b[i]):
        check1 = -1
        
        
    if ord(a[i]) == ord(b[i]):
        check1 = 0

    if(check1 ==1 or check1 ==-1):
        break

print(check1)



