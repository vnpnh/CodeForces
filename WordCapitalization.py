a = str(input())
temp= a
d = len(a)
b = ord(a[0])
c = []

def converts(a):
    first = chr(a)

    for i in range(1,d):
        c.append(temp[i])

    e = "".join(c)
    print(first+e)
if(ord(a[0])>= ord("a") and ord(a[0]) <= ord("z")):
    a =ord(a[0]) -32
    converts(a)
    
else:
    print(temp)




