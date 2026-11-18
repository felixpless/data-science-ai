# Chapter 01 — Python Fundamentals

**Completed · 8/8 modules**

Work through the lessons in order, from references and loops to a tested CSV order analysis. Each lesson links to its exercise and gives a command to run it.

| Lesson | What you practise |
| --- | --- |
| [01 — Python Basics](01-basics/README.md) | Follow a list through mutation, copying, and reassignment. Compare the object IDs after a new list is assigned. |
| [02 — Control Flow](02-control-flow/README.md) | Accumulate shipment weights, filter delivered revenue, and use thresholds of 100 and 200 to classify orders. |
| [03 — Functions](03-functions/README.md) | Pass one order or a collection to a function. Compare quoted shipping costs, delivery status, and realized profit. |
| [04 — Data Structures](04-data-structures/README.md) | Look up fields in shipment records, unpack coordinates, and use comprehensions to build order lists, sets, and dictionaries. |
| [05 — Modules](05-modules/README.md) | Trace how a calculation in one file becomes available to a caller through an import. |
| [06 — Object-Oriented Programming](06-oop/README.md) | Use Order and Shipment instances to see how changing delivery status affects the results of method calls. |
| [07 — Error Handling](07-error-handling/README.md) | Handle an invalid order and continue processing the next record. |
| [08 — Professional Python](08-professional-python/README.md) | Read order data, validate individual rows, and test the financial metrics calculated from delivered orders. |

## Final exercise and tests

Run these commands from the repository root with pytest installed.

```sh
python3 01-python/08-professional-python/python_final_exercise.py
python3 -m pytest -q 01-python
```

The [final exercise](08-professional-python/python_final_exercise.py) calculates delivered revenue, profit, and delivery rate from the sample CSV. The [professional Python lesson](08-professional-python/README.md) explains the expected results.

## Reference

Use the [Python cheatsheet](PYTHON_01_CHEATSHEET.md) for review. The [original exercises and notes](_archive/original-exercises/) preserve the files that were reorganized, including the [combined practice script](_archive/original-exercises/01-basics/objects_and_variables.py).
