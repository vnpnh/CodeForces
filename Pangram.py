n = int(input())
a = str(input().lower())


d= set()
c = [d.add(i) for i in a if i not in d]

if len(d) == 26:
    print("YES")
else:
    print("NO")
