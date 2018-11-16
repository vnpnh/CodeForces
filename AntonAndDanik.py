a = int(input())
b = str(input())

v = [i for i in b if i == "D"]
c = [i for i in b if i == "A"]

if len(v) > len(c):
    print("Danik")
if len(v) < len(c):
    print("Anton")
if len(v) == len(c):
    print("Friendship")
