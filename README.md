# Tap-Counter

**A zero-typing sales counter for small shops that sell without bills.** One button per item (Samosa · Chai ·
Badam milk) on an ESP32 → AWS → a kitchen screen and a night summary that shows whether the cash matches the sales.

Built in 12 chapters that follow a university Cloud Computing course: from a single button to IoT, serverless,
containers, Infrastructure as Code, monitoring and cost.

## Try it now (phone app, no hardware)
**Live:** https://bsharan.github.io/tap-counter/ (open on a phone). One tap per sale, undo, running total, and a night
summary: enter the UPI and cash totals and it shows the gap. Telugu + English, WhatsApp share, data stays on the phone.

## Chapters
| Chapter | What it adds |
|---|---|
| [01 – First device](01-cloud-revolution/) | ESP32 blinking an LED, simulated in Wokwi |

## Status
v0.1 in progress. The core logic is tested (CI badge goes here after the first push).

## Run the tests
```bash
pip install pytest
python -m pytest -q
```

## Try a demo day
```bash
python demo.py
```

See `SPEC.md` for what it must do, and `ROADMAP.md` for the plan.

Author: Bediga Sharan, Assistant Professor, CSE, SR University, Warangal.
