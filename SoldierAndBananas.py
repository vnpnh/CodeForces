a = list(map(int,input().split()))

price = a[0]
money = a[1]
item = a[2]
arr = []
total = 0
check = 0
for i in range(1,item+1):
    check = price *i
    
    total += check



if money > total:
    print("0")
else:
    print(abs(total-money))
