a = "1+1+3+1+3"
div = int(len(a)/2)
list_a = list(a)


list_a.sort()
last = list_a[div:]
print("+".join(last))
