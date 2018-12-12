n = int(input())

room = [[int(i) for i in input().split()] for j in range(n)]

c = list(map(lambda x:abs(x[0]-x[1]),room))
free = list(filter(lambda x:x>1,c))

print(len(free))
