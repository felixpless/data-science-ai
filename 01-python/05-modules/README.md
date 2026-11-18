# 05 — Modules

Trace how a calculation in one file becomes available to a caller through an import.

## Run the exercise

From this lesson folder, run `python3 module_practice.py`. [Open the exercise](module_practice.py).

[financial_metrics.py](financial_metrics.py) defines the per-order profit and batch totals. The batch revenue includes every order. Realized profit counts only delivered orders.

[module_practice.py](module_practice.py) imports the module and handles valid and malformed records. Run [import_test.py](import_test.py) to see the effect of the main guard. Importing the module skips the processing loop.

From this lesson folder, you can repeat the original per-order import exercise:

```python
from financial_metrics import calculate_realized_profit
from module_practice import orders

for order in orders:
    print(order["order_id"], calculate_realized_profit(order))
```

[Chapter overview](../README.md)
