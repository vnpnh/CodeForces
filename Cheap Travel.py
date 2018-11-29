import math
total_ride,special_ticket,ticket_price,special_price = list(map(int,input().split()))


price1 = total_ride * ticket_price

rest = int(total_ride/special_ticket)
check = total_ride%special_ticket

if check > 0:
    price2 = (special_price*rest) + (check*ticket_price)
else:
    price2 = rest *special_price

rests = math.ceil(total_ride/special_ticket)
price3  = special_price * rests

print(min([price1,price2,price3]))
    
