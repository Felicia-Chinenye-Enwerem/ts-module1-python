#OR I attempt to get to the same result using a different code set. 
amount_due= 50
valid_coin= (25, 10, 5)

while amount_due > 0:
    print(f"Balance is: {amount_due}")
    coin= int(input("Insert coins: "))
    if coin in valid_coin:
       amount_due -= coin
       print("Change owed:", abs(amount_due))
    else:
        print("Invalid inserted coin. Insert only: 25, 10, 5.")


    

