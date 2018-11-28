row,column = list(map(int,input().split()))

odd = ["#" for i in range(column)]

even1 = ["."for i in range(column-1)]
even1 += "#"

even2 = ['.' for i in range(column-1)]
even2.insert(0,"#")

res = []
check = False
for i in range(1,row+1):
    
    if i %2 ==1:
        res.append(odd)
    elif i %2 ==0 and check == False:
        check =  True
        res.append(even1)
    else:
        res.append(even2)
        check = False
for i in res:
	for j in i:
		print(j,end="")
	print()
