
total_price = 0
item_number = int(input("Number of items: "))
while item_number <= 0:
    item_number = int(input("Number of items: "))
for x in range(item_number):
    total_price += float(input("Price of item: "))
if total_price > 100:
    total_price *= 0.9
print("Total price for", item_number, "items is $" + str(total_price))
