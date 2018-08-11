TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

print("Electricity bill estimator 2.0")
tariff = int(input("Which tariff? 11 or 31: "))
while tariff not in [11, 31]:
    tariff = int(input("Which tariff? 11 or 31: "))
if tariff == 11:
    dollars_per_kWh = TARIFF_11
else:
    dollars_per_kWh = TARIFF_31
kWh_daily_use = float(input("Enter daily use in kWh: "))
billing_days = int(input("Enter number of billing days: "))
bill = round(dollars_per_kWh * kWh_daily_use * billing_days, 2)
print("Estimated bill: $" + str(bill))
