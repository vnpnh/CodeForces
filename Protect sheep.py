a = list(map(int,input().split()))
row = a[0]
column = a[1]

game = []

for i in range(row):
    c = str(input())
    game.append([c])



new = [[j.replace(".","D")]for i in game for j in i]

news = []

for i in new:
    for j in i:
        temp = ",".join(j)
        temps = temp.split(",")
        news.append(temps)

secure = True
find = "S"
found = False

check = 0

if column > 1:
    for i in news:
        
        if secure == False:
            break
        if i[0] == find:
                
                if i[1] == "S" or i[1] == "D":
                    
                    secure = True
                else:
                    secure = False
                    break
        if i[column-1] == find:
            
            if i[column-2] == "W":
                secure = False
                break
            else:
                secure = True

        if secure == False:
            break
        for j in range(1,column-1):
            if i[j] == find:
                secure = False
                
                if (i[j+1] == "S" or i[j+1] == "D"):
                    
                    secure = True
                else:
                    secure = False
                    break
                if (i[j-1] == "S" or i[j-1] == "D"):
                    
                    secure = True
                else:

                    secure = False
                    break
                if secure ==  False:
                    break

                    
            if secure== False:
                break
            
                
          
revert = list(zip(*news))       
    

if row > 1:
    for i in revert:
        
        if secure == False:
            break
        if i[0] == find:
                
                if i[1] == "S" or i[1] == "D":
                    
                    secure = True
                else:
                    secure = False
                    break
        if i[row-1] == find:
            
            if i[row-2] == "W":
                secure = False
                break
            else:
                secure = True

        if secure == False:
            break
        for j in range(1,row-1):
            if i[j] == find:
                secure = False
                
                if (i[j+1] == "S" or i[j+1] == "D"):
                    
                    secure = True
                else:
                    secure = False
                    break
                if (i[j-1] == "S" or i[j-1] == "D"):
                    
                    secure = True
                else:

                    secure = False
                    break
                if secure ==  False:
                    break

                    
            if secure== False:
                break


    

      





if secure:
    print("Yes")
    for j in news:
        for i in j:
            print(i,end="")
        print()
else:
    print("No")
