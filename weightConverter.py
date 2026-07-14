# Python weight converter

weight = float(input("Enter your weight: "))
unit = input("Kilograms or pounds? (kg or lbs): ")

if unit == "kg":
    weight *= 2.205
    print(f"Your weight is: {round(weight, 2)}lb(s)")
elif unit == "lbs":
    weight /= 2.205
    print(f"Your weight is: {round(weight, 2)}kg")
else:
    print(f"{unit} is not a valid unit of measurement.")
