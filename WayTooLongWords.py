number = int(input())

for i in range(number):
    words = input()
    first = words[0]
    last = words[len(words)-1]
    if 10 >= len(words):
        print(words)
        
    else:
        total = len(words) - 2
        totals = first+str(total)+last
        print(totals)
