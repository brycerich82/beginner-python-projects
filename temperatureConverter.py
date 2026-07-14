# Temperature Conversion Program

temp = float(input("Enter the temperature: "))
unit1 = input("Is this temperature in Fahrenheit, Celsius, or Kelvin? (F/C/K): ")
unit2 = input("What unit would you like to convert to? (F/C/K): ")

if unit1.upper() == "F" and unit2.upper() == "C":
    temp = (temp - 32) * (5 / 9)
    print(f"The temperature in Celsius is: {round(temp, 1)}°C.")
elif unit1.upper() == "F" and unit2.upper() == "K":
    temp = (temp - 32) * (5 / 9) + 273.15
    print(f"The temperature in Kelvin is: {round(temp, 1)}°K.")
elif unit1.upper() == "C" and unit2.upper() == "F":
    temp = (temp * (9 / 5)) + 32
    print(f"The temperature in Fahrenheit is: {round(temp, 1)}°F.")
elif unit1.upper() == "C" and unit2.upper() == "K":
    temp += 273.15
    print(f"The temperature in Kelvin is: {round(temp, 1)}°K.")
elif unit1.upper() == "K" and unit2.upper() == "F":
    temp = (temp - 273.15) * (9 / 5) + 32
    print(f"The temperature in Fahrenheit is: {round(temp, 1)}°F.")
elif unit1.upper() == "K" and unit2.upper() == "C":
    temp -= 273.15
    print(f"The temperature in Celsius is: {round(temp, 1)}°C.")
else:
    print(
        f"Either {unit1.upper()} or {unit2.upper()} is not a valid unit of measurement."
    )
