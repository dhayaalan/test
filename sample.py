weight=int(input("Weight: "))
unit=input("(L)pounds or (K)kg:")
if unit.upper()=="L":
    converted=weight*0.45
    print(f"you are {converted} kilo")
else :
    converted=weight/0.45
    print(f"you are {converted} in pounds")
