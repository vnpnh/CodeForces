a = str(input())
b = str(input())
c = str(input())

temp1 = [ord(i) for i in a]
temp2 = [ord(i) for i in b]
temp3 = [ord(i) for i in c]
a1 = sorted(temp1+temp2)
if sum(temp1) + sum(temp2) == sum(temp3) and (a1 == sorted(temp3)):
    print("YES")
else:
    print("NO")
