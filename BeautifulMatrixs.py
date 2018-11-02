b = []

def search(a):
    check = 0
    position = 0
    for j in range(5):
        for i in range(5):
            if(b[j][i] == 0):
                check+=1
                
            else:
                position = check
                break
    return position
'''
0 0 0 0 0
0 0 0 0 1
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
'''
for i in range(5):
    a = list(map(int,input().strip().split()))
    b.append(a)


position = search(b)
center = 12
"""
#posisi (1,1)-(5,1)
if position == 0:
    print("4")
elif position == 1:
    print("3")
elif position == 2:
    print("2")
elif position == 3:
    print("3")
elif position == 4:
    print("4")

elif position == 5:
    print("3")
elif position == 6:
    print("2")
elif position == 7:
    print("1")
elif position == 8:
    print("2")
elif position == 9:
    print("3")


elif position == 10:
    print("2")
elif position == 11:
    print("1")
elif position == 12:
    print("0")
elif position == 13:
    print("1")
elif position == 14:
    print("2")

elif position == 15:
    print("3")
elif position == 16:
    print("2")
elif position == 17:
    print("1")
elif position == 18:
    print("2")
elif position == 19:
    print("3")
   

elif position == 20:
    print("4")
elif position == 21:
    print("3")
elif position == 22:
    print("2")
elif position == 23:
    print("3")
elif position == 24:
    print("4")
"""

            

def matrixs(position):
    check = 0
    for i in range(5):
        for j in range(5):
            if position[i][j] == 1:
                check = abs(i-2)+abs(j-2)


    return check



print(matrixs(b))
    
