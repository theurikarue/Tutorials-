weight = float(input("Weight: "))
unit = input("(k) Kgs or (l) Lbs: ")

if unit.lower() == 'k':
    converted_weight = weight * 2.20462
    print("Converted weight:", converted_weight, "Lbs")
elif unit.lower() == 'l':
    converted_weight = weight / 2.20462
    print("Converted weight:", converted_weight, "Kgs")
else:
    print("Invalid unit! Please choose either 'k' or 'l'.")


    
