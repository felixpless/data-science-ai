shipments = [
    {"destination": "Vienna", "weight_kg": 420},
    {"destination": "Munich", "weight_kg": 180},
    {"destination": "Prague", "weight_kg": 250},
]

total_weight = 0
overweight_total = 0
for shipment in shipments:
    print(shipment["destination"])
    total_weight += shipment["weight_kg"]
    if shipment["weight_kg"] > 200:
        overweight_total += shipment["weight_kg"]

print("Total shipment weight (kg):", total_weight)
print("Average weight (kg):", round(total_weight / len(shipments)))
print("Weight of shipments over 200 kg:", overweight_total)

orders = [
    {"order_id": "O-101", "revenue": 120, "cost": 80, "delivered": True},
    {"order_id": "O-102", "revenue": 75, "cost": 50, "delivered": False},
    {"order_id": "O-103", "revenue": 210, "cost": 130, "delivered": True},
    {"order_id": "O-104", "revenue": 95, "cost": 60, "delivered": True},
]

delivered_revenue = 0
for order in orders:
    if order["delivered"]:
        print(order["order_id"], "Delivered")
        delivered_revenue += order["revenue"]
    else:
        print(order["order_id"], "Not delivered")

    if order["revenue"] >= 200:
        category = "High"
    elif order["revenue"] >= 100:
        category = "Medium"
    else:
        category = "Low"
    print(order["order_id"], category)

print("Delivered revenue:", delivered_revenue)
