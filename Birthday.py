a = list(map(int,input().rstrip().split()))
# a[0] quantity of different coins
# a[1] total of ivans friends
# a[2] ivan collection
# a[3] that must be new in Ivan's collection.
#atau minimal coin

coins = a[0]
friends = a[1]
collections = a[2]
wajib = a[3]


current = coins -collections
last = current/friends
now = (current/wajib) - (friends/wajib)
wajibs = current / wajib

if current < friends:
    print("-1")
elif wajibs < last:
    print("-1")
else:
    print(int(last))
        



    
    
