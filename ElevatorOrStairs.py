a = list(map(int,input().split()))

actualFloor = a[0] #tempat asal
targetLocation = a[1] #tempat destinasi
elevatorLocated = a[2] #lokasi elevator
passTwoFloorStair = a[3] #waktu yang dibutuhkan Masha untuk
#melewati antara dua lantai dengan tangga
passTwoFloorElevator = a[4]  #waktu yang dibutuhkan lift untuk melewati dua lantai
openCloseElevator = a[5]
#waktu yang dibutuhkan lift untuk menutup atau membuka pintu.

#1 6 6 2 1 1


totalOpenLose = a[5]*3

timeEle = 0
jarakDestinasi = actualFloor - targetLocation
jarakDestinasiTangga = actualFloor - targetLocation
jarakElevator = actualFloor - elevatorLocated
jarakDestinasi = abs(jarakDestinasi)

otwToActual = actualFloor - elevatorLocated
timeEle = passTwoFloorElevator *abs(otwToActual)
timeStairs = jarakDestinasi*passTwoFloorStair

totalTimesEle = timeEle +(jarakDestinasi*passTwoFloorElevator)+totalOpenLose


jarakDestinasiTangga*= passTwoFloorStair

jarakDestinasiTangga = abs(jarakDestinasiTangga)
if totalTimesEle <= abs(timeStairs):
    print("YES")
else:
    print("NO")










    




    
    
        

