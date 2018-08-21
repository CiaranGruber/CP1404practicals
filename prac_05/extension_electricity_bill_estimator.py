TARIFF_11 = 0.244618
TARIFF_31 = 0.136928
TARIFFS = {'11': 0.244618, '31': 0.136928}

print("Electricity bill estimator 2.0")

tariff = input("Which tariff? ")
while tariff not in TARIFFS:
    tariff = input("Which tariff? ")
dollars_per_kWh = TARIFFS[tariff]

kWh_daily_use = float(input("Enter daily use in kWh: "))
billing_days = int(input("Enter number of billing days: "))
bill = round(dollars_per_kWh * kWh_daily_use * billing_days, 2)
print("Estimated bill: $" + str(bill))
