a = int(input())
scorem = 0
scorec = 0
for i in range(a):
    m,c = input().split()
    if m > c:
        scorem +=1
    if m < c:
        scorec+=1


if scorem > scorec:
    print("Mishka")
if scorem < scorec:
    print("Chris")
if scorem == scorec:
    print("Friendship is magic!^^")
    
