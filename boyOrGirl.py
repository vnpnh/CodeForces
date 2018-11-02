a = str(input())

b = sorted(a)
check = 0
for i in range(len(a)-1):
    if b[i] == b[i+1]:
        check+=1

total = abs(check - len(a))
if total %2 ==0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
