"""
Electricity bill estimator that estimates bill according to user input

Electricity Bill Estimator. Created by Ciaran Gruber - 21/08/18
"""

TARIFFS = {'11': 0.244618, '31': 0.136928}


def main():
    """Electricity bill estimator"""
    print("Electricity bill estimator 2.0")
    tariff = input("Which tariff? ")
    while tariff not in TARIFFS:
        tariff = input("Which tariff? ")
    dollars_per_kWh = TARIFFS[tariff]
    kWh_daily_use = float(input("Enter daily use in kWh: "))
    billing_days = int(input("Enter number of billing days: "))
    bill = round(dollars_per_kWh * kWh_daily_use * billing_days, 2)
    print("Estimated bill: $" + str(bill))


main()
