b = str(input())
c = str(input())
x = list(" ".join(b))
y = list(" ".join(c))

list1 = [i for i in x if i.isdigit()]
list2 = [i for i in y if i.isdigit()]


tot = list(zip(list1,list2))
res = []
temp = "0"
for i in tot:
    
    if i[0] == '0' and i[1] == '0' :
        
        res.append(str(temp))
    elif i[0] == '1' and i[1] == '0':
        temp = "1"
        res.append(str(temp))
        temp = "0"
    elif i[0] == '0' and i[1] == '1':
        temp = "1"
        res.append(str(temp))
        temp = "0"
    
        
    elif i[0] == '1' and i[1] == '1':
        temp = "0"
        res.append(str(temp))
        
    
print("".join(res))    
