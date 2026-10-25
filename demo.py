"""A day at Raju Tea Stall: taps during the rush, then the night summary."""
from tapcounter.core import Shop

shop = Shop("Raju Tea Stall", {"samosa": 15, "chai": 10, "badam_milk": 30})
shop.tap("samosa", 140)
shop.tap("chai", 300)
shop.tap("badam_milk", 50)

print(shop.summary(upi_total=4200, cash_total=2100)["text"])
