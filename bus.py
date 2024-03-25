# the location and their prices
iyana_paja = 100
ikotun = 200
egbeda = 100
ikeja_along = 300
oshodi = 400


print("1. Iyana paja - 100\n2. Ikotun - 200\n3. Egbeda - 100\n4. Ikeja-along - 300\n5. Oshodi - 400\n How far which side you dey go? ...Answer me jare")
reply = str(input(">> ")).lower()
print("I no get change oh, hold your change, How much dey your hand!!!")
res = int(input())
if res < 400:
    print("Oya enter\nDriver dey go!!")
    if reply == "1" or reply == "iyana paja":
        balance =  res - iyana_paja 
        if balance == 0:
            print("you no get change")
        else:
            print(f"your change is ${balance}")
    elif reply == "2" or reply == "ikotun":
        balance = ikotun - res
        if balance == 0:
            print("you no get change")
        else:
            print(f"your change is ${balance}")
    elif reply == "3" or reply == "egbeda":
        balance =  res - egbeda 
        if balance == 0:
            print("you no get change")
        else:
            print(f"your change is ${balance}")
    elif reply == "4" or reply == "ikeja along":
        balance =  res - ikeja_along 
        if balance == 0:
            print("you no get change")
        else:
            print(f"your change is ${balance}")
    elif reply == "5" or reply == "oshodi":
        balance = res - oshodi
        if balance == 0:
            print("you no get change")
        else:
            print(f"your change is ${balance}")
else:
    print("oga comot jare i no get change!!!!!") 



print("Zoooooooommmmm!!!!!!")
    