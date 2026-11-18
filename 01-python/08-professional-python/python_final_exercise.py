import csv
from math import isfinite
from pathlib import Path


def load_orders(file_path: Path = Path(__file__).with_name("orders_final.csv")) -> list[dict]:
    with file_path.open(encoding="utf-8", newline="") as source:
        return list(csv.DictReader(source))


def validate_order(order: dict) -> dict:
    order_id = order.get("order_id")
    if not order_id or not order_id.strip():
        raise ValueError("Missing order ID")

    amounts = {}
    for field in ("revenue", "cost"):
        try:
            amount = float(order[field])
        except (KeyError, TypeError, ValueError) as error:
            raise ValueError(f"Invalid {field}") from error
        if not isfinite(amount) or amount < 0:
            raise ValueError(f"{field} must be finite and non-negative")
        amounts[field] = amount

    delivered = str(order.get("delivered")).strip().lower()
    if delivered not in ("true", "false"):
        raise ValueError("Expected True or False for delivered")

    return {"order_id": order_id, **amounts, "delivered": delivered == "true"}


def process_orders(orders: list[dict]) -> list[dict]:
    valid_orders = []
    for order in orders:
        try:
            valid_orders.append(validate_order(order))
        except ValueError as error:
            print(f"Skipping {order.get('order_id') or '<unknown>'}: {error}")
    return valid_orders


def calculate_kpis(valid_orders: list[dict]) -> dict[str, float]:
    total_revenue = 0.0
    total_cost = 0.0
    delivered_count = 0
    for order in valid_orders:
        if order["delivered"]:
            total_revenue += order["revenue"]
            total_cost += order["cost"]
            delivered_count += 1

    return {
        "total_revenue": total_revenue,
        "total_profit": total_revenue - total_cost,
        "delivery_rate": delivered_count / len(valid_orders) if valid_orders else 0.0,
    }


def main() -> None:
    valid_orders = process_orders(load_orders())
    print(f"Valid orders: {len(valid_orders)}")
    print(calculate_kpis(valid_orders))


if __name__ == "__main__":
    main()
