import re
n = str(input())


rem = re.compile(r'[^abcdfgijkmnpqrstuvwyzx]')
find = rem.findall(n)

hello = ["h","e","l","l","o"]
check = 0
checking = 0
z = 0
for i in hello:
    checking = 0
    for j in range(check,len(find)):
        if i == find[j]:
            check = j+1
            checking =1
            z+=1
           
        if checking ==1:
            break
                    
       
    
if z ==5:
    print("YES")
else:
    print("NO")
        





    
        
