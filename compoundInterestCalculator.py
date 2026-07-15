# Compound Interest Calculator

principle = 0
rate = 0
time = 0
contribution = 0

while True:
    principle = float(input("Enter the principle value in $: "))
    if principle < 0:
        print("Principle can't be negative.")
    else:
        break

while True:
    contribution = float(
        input("Enter annual contribution in $ (assume beginning-of-year payments): ")
    )
    if contribution < 0:
        print("Contribution can't be negative.")
    else:
        break

while True:
    rate = float(input("Enter the expected rate of return in %: "))
    if rate < 0:
        print("rate can't be negative.")
    else:
        break

while True:
    time = int(input("Enter the time in years: "))
    if time <= 0:
        print("time can't be less than or equal to zero.")
    else:
        break

if rate == 0:
    total = principle + contribution * time
else:
    total = principle * pow((1 + rate / 100), time) + contribution * (
        (pow(1 + rate / 100, time) - 1) / (rate / 100)
    ) * (1 + rate / 100)

print(f"\nBalance after {time} year(s) is: ${total:.2f}")
