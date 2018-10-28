a = int(input()) #input angka
b = int(a/2) # di bagi sama a
print("nilai",b,"\n")
if a % 2 == 1: # cek apakah modulus nya 1
    c = a - b #dikurang a yang atas dan b yang atas
    print(a,b,c)
    total = str(b)+str(c) # masukin ke string contoh "1","2"
    lists = list(total) #di jadikan list ["1","2"]
else:
    b = b +1 #tambah 1 agar tidak 0 
    c = a - b #jika atas nya genap maka sini jadi 0 makanya atasnya ditambah
    print(a,b,c) 
    total = str(b)+str(c) # sama kayak di atas
    lists = list(total) # sama
    
ovals = []
for i in range(len(lists)): #looping
    oval = int(lists[i]) #di jadiin integers listnya
    ovals.append(oval) # masukin ke list [1,2]

print(sum(ovals)) # hitung list 1+2
