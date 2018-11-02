a = str(input())

b = 0

for i in range(len(a)):
    if a[i] == "H" or a[i] == "Q" or a[i] == "9":
        b +=1

    

if b>0:
    print("YES")
else:
    print("NO")
