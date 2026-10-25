import pytest

from tapcounter.core import Shop

PRICES = {"samosa": 15, "chai": 10, "badam_milk": 30}


def make_shop():
    return Shop("Raju Tea Stall", PRICES)


def test_tap_adds_one_by_default():
    shop = make_shop()
    shop.tap("samosa")
    assert shop.tap("samosa") == 2


def test_tap_with_quantity():
    shop = make_shop()
    assert shop.tap("chai", 5) == 5


def test_unknown_item_is_rejected():
    shop = make_shop()
    with pytest.raises(ValueError):
        shop.tap("pizza")


def test_zero_quantity_is_rejected():
    shop = make_shop()
    with pytest.raises(ValueError):
        shop.tap("chai", 0)


def test_expected_cash():
    shop = make_shop()
    shop.tap("samosa", 140)   # 2100
    shop.tap("chai", 300)     # 3000
    shop.tap("badam_milk", 50)  # 1500
    assert shop.expected_cash() == 6600


def test_summary_flags_missing_money():
    shop = make_shop()
    shop.tap("samosa", 10)  # 150
    result = shop.summary(upi_total=100, cash_total=20)
    assert result["gap"] == 30
    assert "ALERT" in result["text"]


def test_summary_notes_untapped_sales():
    shop = make_shop()
    shop.tap("chai", 2)  # 20
    result = shop.summary(upi_total=50)
    assert result["gap"] == -30
    assert "not tapped" in result["text"]


def test_summary_all_good():
    shop = make_shop()
    shop.tap("chai", 3)  # 30
    result = shop.summary(cash_total=30)
    assert result["gap"] == 0
    assert "All good" in result["text"]
