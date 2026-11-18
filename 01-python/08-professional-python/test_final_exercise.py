import shutil
import subprocess
import sys
from pathlib import Path

import pytest

from python_final_exercise import calculate_kpis, load_orders, process_orders


def test_calculate_kpis():
    orders = [
        {"revenue": 120.0, "cost": 80.0, "delivered": True},
        {"revenue": 75.0, "cost": 50.0, "delivered": False},
        {"revenue": 200.0, "cost": 130.0, "delivered": True},
    ]

    result = calculate_kpis(orders)

    assert result["total_revenue"] == 320.0
    assert result["total_profit"] == 110.0
    assert result["delivery_rate"] == 2 / 3


def test_calculate_kpis_empty_orders():
    result = calculate_kpis([])

    assert result["total_revenue"] == 0
    assert result["total_profit"] == 0
    assert result["delivery_rate"] == 0.0


def test_sample_csv_from_another_directory(tmp_path, monkeypatch, capsys):
    monkeypatch.chdir(tmp_path)
    valid = process_orders(load_orders())
    assert [order["order_id"] for order in valid] == ["O-101", "O-102", "O-103", "O-104"]
    assert calculate_kpis(valid) == {"total_revenue": 470, "total_profit": 170, "delivery_rate": 0.75}
    messages = capsys.readouterr().out
    assert "O-105" in messages
    assert "O-106" in messages


@pytest.mark.parametrize(("field", "bad_value"), [
    ("cost", "-1"), ("cost", None), ("revenue", "nan"),
    ("revenue", "inf"), ("delivered", "unknown"), ("order_id", ""),
])
def test_invalid_row_does_not_discard_next_order(field, bad_value):
    order = {"order_id": "O-101", "revenue": "120", "cost": "80", "delivered": "False"}
    invalid = {**order, field: bad_value}
    assert process_orders([invalid, order]) == [
        {"order_id": "O-101", "revenue": 120.0, "cost": 80.0, "delivered": False},
    ]


def test_import_without_sample_csv(tmp_path):
    shutil.copy(Path(__file__).with_name("python_final_exercise.py"), tmp_path)
    result = subprocess.run(
        [sys.executable, "-c", "import python_final_exercise"],
        cwd=tmp_path, capture_output=True, text=True, check=True,
    )
    assert result.stdout == result.stderr == ""
