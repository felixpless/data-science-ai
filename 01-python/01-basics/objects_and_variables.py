daily_orders = [124, 156, 143, 189, 201]
original_orders = daily_orders.copy()
daily_orders[2] = 148
daily_orders.append(176)

print("Original orders:", original_orders)
print("Daily orders:", daily_orders)

orders = [100, 200, 300]
backup = orders
print("Same object before reassignment:", orders is backup)

orders = orders + [400]
print("Orders:", orders)
print("Backup:", backup)
print("Object IDs after reassignment:", id(orders), id(backup))
