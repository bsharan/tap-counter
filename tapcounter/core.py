"""Tap-Counter core: count button taps per item and build the owner's night summary."""
from collections import Counter


class Shop:
    def __init__(self, name, prices):
        self.name = name
        self.prices = dict(prices)
        self.counts = Counter()

    def tap(self, item, qty=1):
        """One button press. Returns the item's new count."""
        if item not in self.prices:
            raise ValueError(f"Unknown item: {item}")
        if qty < 1:
            raise ValueError("Quantity must be at least 1")
        self.counts[item] += qty
        return self.counts[item]

    def expected_cash(self):
        return sum(self.prices[item] * n for item, n in self.counts.items())

    def summary(self, upi_total=0, cash_total=0):
        """Night report: what was sold, what should be in hand, and the gap."""
        expected = self.expected_cash()
        received = upi_total + cash_total
        gap = expected - received

        lines = [f"{self.name}: today's sales"]
        for item, price in self.prices.items():
            n = self.counts[item]
            lines.append(f"  {item}: {n} x Rs {price} = Rs {n * price}")
        lines.append(f"Expected Rs {expected} | Received Rs {received} (UPI + cash) | Gap Rs {gap}")

        if gap > 0:
            lines.append("ALERT: money missing. Check with staff.")
        elif gap < 0:
            lines.append("Note: more money than taps. Some sales were not tapped.")
        else:
            lines.append("All good.")

        return {"expected": expected, "received": received, "gap": gap, "text": "\n".join(lines)}
