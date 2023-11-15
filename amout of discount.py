number=float(input("enter the number: "))
if number >100:
    DISCOUNT = number*10/100
else:
    DISCOUNT = number*5/100
    
print("Your total amount is "  + str(number - DISCOUNT))