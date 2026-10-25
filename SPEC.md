# Tap-Counter: Spec v0.1 (the cloud brain, no hardware yet)

**User:** owner of a small tea/snack stall that sells without bills.

## Must do
1. A **tap** on an item button adds to that item's count (default 1, or a given quantity).
2. Unknown items or a quantity below 1 are **rejected** with a clear error. A wrong button must never corrupt the count.
3. **Expected cash** = sum of (count × price) for every item.
4. **Night summary:** the owner enters the UPI total and the cash total. The system shows each item's count, the expected
   amount, the received amount and the **gap**.
5. Gap > 0 → **ALERT: money missing**. Gap < 0 → note: **sales were probably not tapped**. Gap = 0 → all good.

## Done when
All tests in `tests/` pass.
