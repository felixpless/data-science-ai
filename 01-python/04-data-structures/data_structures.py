customer = {"customer_id": "C1024", "city": "Vienna", "orders": 7, "revenue": 842.50}
print("Customer revenue:", customer["revenue"])

shipment = {
    "shipment_id": "S-2048",
    "origin": "Berlin",
    "destination": "Vienna",
    "weight_in_kgs": 420,
    "delivered": False,
}
print(shipment["destination"], shipment["delivered"])
shipment["delivered"] = True
shipment["destination"] = "Witzehausen"
shipment["delivery_time"] = "14:35"
print(shipment)

shipments = [
    {"shipment_id": "S-1001", "origin": "Berlin", "destination": "Vienna", "weight_kg": 420},
    {"shipment_id": "S-1002", "origin": "Hamburg", "destination": "Munich", "weight_kg": 180},
    {"shipment_id": "S-1003", "origin": "Berlin", "destination": "Prague", "weight_kg": 250},
]
print("Hamburg to Munich (kg):", shipments[1]["weight_kg"])

coordinates = (52.52, 13.40)
latitude, longitude = coordinates
print("Latitude and longitude:", latitude, longitude)

orders = [
    {"order_id": "O-101", "revenue": 120, "cost": 80, "delivered": True},
    {"order_id": "O-102", "revenue": 75, "cost": 50, "delivered": False},
    {"order_id": "O-103", "revenue": 210, "cost": 130, "delivered": True},
    {"order_id": "O-104", "revenue": 95, "cost": 60, "delivered": True},
]

order_ids = [order["order_id"] for order in orders]
delivered_ids = [order["order_id"] for order in orders if order["delivered"]]
delivered_profits = [order["revenue"] - order["cost"] for order in orders if order["delivered"]]
high_revenue_ids = [order["order_id"] for order in orders if order["revenue"] >= 100]
revenue_by_order = {order["order_id"]: order["revenue"] for order in orders}
delivered_profit_by_order = {
    order["order_id"]: order["revenue"] - order["cost"] for order in orders if order["delivered"]
}
delivery_status = {order["delivered"] for order in orders}
categories = ["High" if order["revenue"] >= 100 else "Standard" for order in orders]
category_by_order = {
    order["order_id"]: "High" if order["revenue"] >= 100 else "Standard" for order in orders
}

print("Order IDs:", order_ids)
print("Delivered:", delivered_ids, delivered_profits)
print("High revenue:", high_revenue_ids)
print("Revenue and realized profits:", revenue_by_order, delivered_profit_by_order)
print("Distinct delivery states:", delivery_status)
print("Revenue categories:", categories, category_by_order)
