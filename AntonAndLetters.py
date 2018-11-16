a = str(input())
b = list("".join(a))
c = [i for i in b if i.isalpha()]
print(len(set(c)))
