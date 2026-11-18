# 08 — Professional Python

Read order data, validate individual rows, and test the financial metrics calculated from delivered orders.

## Run the exercise

From this lesson folder, run `python3 python_final_exercise.py`. [Open the exercise](python_final_exercise.py).

## Practice files

| Topic | Exercise |
| --- | --- |
| Type annotations | [type_hints.py](type_hints.py) |
| Extracting and testing a calculation | [refactoring_practice.py](refactoring_practice.py) · [test_metrics.py](test_metrics.py) |
| Log levels | [logging_practice.py](logging_practice.py) |
| Paths and file handling | [pathlib_practice.py](pathlib_practice.py) reads [order.json](order.json). [file_handling.py](file_handling.py) parses [orders.txt](orders.txt) as CSV. |
| JSON round trip | Running [json_practice.py](json_practice.py) writes its example to [order.json](order.json) and reads it back. |

## Final exercise

[python_final_exercise.py](python_final_exercise.py) reads [orders_final.csv](orders_final.csv) beside the script. Each row needs an order ID, finite non-negative revenue and cost, and a True or False delivery flag. A rejected row is reported and processing continues.

The sample has six orders. O-105 has negative revenue and O-106 has a nonnumeric cost. Of the four valid orders, three were delivered. Delivered revenue is 470, profit is 170, and the delivery rate is 3/4.

[test_final_exercise.py](test_final_exercise.py) checks the KPIs, invalid rows, and file access. From this folder, run `python3 -m pytest -q`.

[Chapter overview](../README.md)
