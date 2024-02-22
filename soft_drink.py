"""Soft Drink shop"""

pepsi = 300
mirinda = 250
seven_up = 350
coke = 300
ab = pepsi + mirinda
bc = mirinda + seven_up
bd = mirinda + coke
cd = seven_up + coke
ad = pepsi + coke
ca = seven_up + pepsi
print("Hello, what are you buying from us today?")
print("We have :\n1. Pepsi #300\n2. Mirinda #250\n3. 7up #350\n4. Coke #300\n5. pepsi + mirinda\n6. irinda + seven_up\n7. mirinda + coke\n8. seven_up + coke\n9. pepsi + coke\n10. seven_up + pepsi")
product = str(input()).lower()
if product == "1" or product =="pepsi":
    print("How many are you buying")
    quantity = int(input())
    total_cost = pepsi * quantity
    print(f"Your total cost is NGN{total_cost}")
elif product == "2" or product == "mirinda":
    print("How many are you buying")
    quantity = int(input())
    total_cost = mirinda * quantity
    print(f"Your total cost is NGN{total_cost}")
elif product == "3" or product == "7up":
    print("How many are you buying")
    quantity = int(input())
    total_cost = seven_up * quantity
    print(f"Your total cost is NGN{total_cost}")
elif product == "4" or product == "coke":
    print("How many are you buying")
    quantity = int(input())
    total_cost = coke * quantity
    print(f"Your total cost is NGN{total_cost}")
elif product == "pepsi and mirinda" or product == "5":
    print("How many are you buying")
    quantity = int(input())
    total_cost = ab * quantity
    print(f"Your total cost is NGN{total_cost}")
elif product == "mirinda and 7up" or product == "6":
    print("How many are you buying")
    quantity = int(input())
    total_cost = bc * quantity
    print(f"Your total cost is NGN{total_cost}")
elif product == "mirinda and coke" or product == "7":
    print("How many are you buying")
    quantity = int(input())
    total_cost = bd * quantity
    print(f"Your total cost is NGN{total_cost}")
elif product == "7up and coke" or product == "8":
    print("How many are you buying")
    quantity = int(input())
    total_cost = cd * quantity
    print(f"Your total cost is NGN{total_cost}")
elif product == "pepsi and coke" or product == "9":
    print("How many are you buying")
    quantity = int(input())
    total_cost = ad * quantity
    print(f"Your total cost is NGN{total_cost}")
elif product == "7up and pepsi" or product == "10":
    print("How many are you buying")
    quantity = int(input())
    total_cost = ca * quantity
    print(f"Your total cost is NGN{total_cost}")
else:
    print("Invalid shop request")
print("What type of payment are your making\n1. Cash payment\n2. Bank payment")
reply = str(input(">> "))
if reply == "1" or reply == "cash payment":
    cash = int(input("How much cash are you paying "))
    balance = cash - total_cost
    print(f"Your balance is {balance}")
elif reply == "2" or reply == "bank payment" :
        print(f"We have successfully deducted NGN{total_cost} from your account")
else:
    print("Invalid request")
print("Thanks for shoping with us ❤️")