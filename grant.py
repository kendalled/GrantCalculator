# Grant's Cost Calculator Tool

base_pin = 3.00
base_coin = 3.50
base_chain = 3.24
qty = 0
res = 0

option = input("Type pin, coin, or keychain and press enter: ")

if(option == "pin"):
    qty = int(input("\nEnter your desired pin quantity, 100 - 1000: "))
    res = qty * base_pin
    
elif(option == "coin"):
    qty = int(input("\nEnter your desired coin quantity, 100 - 1000: "))
    res = qty * base_coin

else:
    qty = int(input("\nEnter your desired keychain quantity, 100 - 1000: "))
    res = qty * base_chain



print("Your quote is: {}".format(res))
