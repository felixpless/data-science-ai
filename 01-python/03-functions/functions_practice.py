def classify_order(revenue):
    if revenue >= 200:
        return " has a High Value"
    if revenue >= 100:
        return " has a Medium Value"
    return " has a Low Value"


def calculate_shipping_cost(weight_kg, distance_km):
    return weight_kg * 0.05 + distance_km * 0.02


def weight_based_cost(weight_kg, fuel_surcharge):
    return weight_kg * 0.05 + fuel_surcharge


def calculate_cost(weight_kg, distance_km, fuel_surcharge=5):
    return calculate_shipping_cost(weight_kg, distance_km) + fuel_surcharge


def get_order_status(order):
    return "Delivered" if order["delivered"] else "Not Delivered"


def calculate_profit(order):
    return order["revenue"] - order["cost"]


def calculate_realized_profit(order):
    if not order["delivered"]:
        return 0
    return calculate_profit(order)


def calculate_financial_metrics(orders):
    total_revenue = 0
    total_realized_profit = 0
    for order in orders:
        total_revenue += order["revenue"]
        total_realized_profit += calculate_realized_profit(order)
    return {"revenue": total_revenue, "realized_profit": total_realized_profit}


def main():
    orders = [
        {"order_id": "O-101", "revenue": 120, "cost": 80, "delivered": True},
        {"order_id": "O-102", "revenue": 75, "cost": 50, "delivered": False},
        {"order_id": "O-103", "revenue": 210, "cost": 130, "delivered": True},
        {"order_id": "O-104", "revenue": 95, "cost": 60, "delivered": True},
    ]
    for order in orders:
        print(order["order_id"] + classify_order(order["revenue"]), get_order_status(order))
        print("Profit:", calculate_profit(order), "Realized:", calculate_realized_profit(order))
    print(calculate_financial_metrics(orders))
    print("Weight and distance:", calculate_shipping_cost(420, 680))
    print("Weight and surcharge:", weight_based_cost(100, 5))
    print("Default surcharge:", calculate_cost(420, 680))
    print("Custom surcharge:", calculate_cost(weight_kg=420, distance_km=680, fuel_surcharge=12))


if __name__ == "__main__":
    main()
