# Grant's Cost Calculator Tool

coins =	{
  3.0 : 6.37,
  2.75 : 5.66,
  2.5 : 4.95,
  2.25 : 4.37,
  2.0 : 3.52,
  1.75 : 3.22,
  1.5 : 2.96,
}

# Resets Vars
qty = 0
res = 0

# Support for Multiple Items
option = input("Type pin, coin, or keychain and press enter: ")

if(option == "coin"):
    # Base Price Based on Size
    base_price = coins.get(float(input("\nEnter your desired size, 1.5 - 3.0 (inches): ")))

    # Plating Calculation
    plating = input("Dual Plated? Yes or No: ")
    if(plating == "yes" or plating == "Yes"):
        base_price += .30
        
    # Custom Edge Calculation
    edge = input("Custom Edge? Yes or No: ")
    if(edge == "yes" or edge == "Yes"):
        base_price += .70
        
    # Quantity Calculation
    qty = int(input("\nEnter your desired quantity, 100 or more: "))

    # Final Cost
    res = qty * base_price

# Print Out to User
print("-------------------------------")
print("Your quote is: ${}".format(res))
