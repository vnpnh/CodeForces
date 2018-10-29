a = input()
check = 0
for i in range(len(a)-1):
    if a[i] == a[i+1]:
        check += 1
    else:
       if check >=6:
           break
       else:
           
           check =0

if check >= 6:
    print("YES")
else:
    print("NO")
