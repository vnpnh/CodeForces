a = int(input())
b = str(input())
check = 0
uncheck = 0

last = len(b)
for i in range(len(b)):
    for j in range(len(b)):
        if b[i] == b[j]:
            check +=1
        else:
            uncheck += 1

if uncheck > check and a >= int(last):
    print("YES")
    print(b[:4])
elif a < int(last) or uncheck < check:
    print("NO")
