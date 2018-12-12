n = str(input())
a = ",".join(n)
b = a.split(",")

check = 0
for i in range(len(b)):
    if b[i] == "4" or b[i] == "7":
        check = 1
    else:
        check = 0
        break
        
c = int(n)
if c % 4 == 0 or c %7 == 0 or  c % 47 == 0 or c %74 == 0 or c %477 == 0:
    check =1


if check == 1:
    print("YES")
else:
    print("NO")
