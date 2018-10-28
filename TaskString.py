a = str(input())
a = a.lower()
temp = []
for i in range(len(a)):
    if a[i] == "a" or a[i] == "e" or a[i] == "o" or a[i] == "i" or a[i] == "u":
            pass
    else:
        temp.append(a[i])

print(temp)
d = ".".join(temp)
print("."+d)
