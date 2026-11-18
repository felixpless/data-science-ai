# 07 — Error Handling

Handle an invalid order and continue processing the next record.

## Run the exercise

From this lesson folder, run `python3 error_handling_practice.py`. [Open the exercise](error_handling_practice.py).

The first row returns a realized profit of 40. Follow the remaining rows through the three handlers.

| Example | Exception | Cause |
| --- | --- | --- |
| O-105 | `KeyError` | Missing cost |
| O-106 | `TypeError` | Cost stored as the string `80 EUR` |
| O-107 and O-108 | `ValueError` | Negative revenue or cost |

[Chapter overview](../README.md)
