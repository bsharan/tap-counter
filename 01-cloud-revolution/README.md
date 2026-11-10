# Chapter 1: First device
An ESP32 blinking an LED, simulated in the browser (Wokwi). No hardware needed.

Try it: https://wokwi.com/projects/480137648567574529

Wiring (ESP32 DevKitC): LED anode (long leg) → pin **2** on the right column (GPIO2; the "D2" label on the left is a flash pin), cathode (short leg) → GND.
In Tap-Counter, this LED becomes the "sale recorded" light.

## Part 2: the button that counts sales
`button.ino` + `diagram.json` (paste both into a new Wokwi ESP32 project). Each press prints `Sale! Count = N` and flashes the LED.
Ideas used: **state** (`wasPressed`), **edge detection** (count only the moment the button goes down), **debouncing** (ignore 20 ms of contact bounce).
Tested 10 Nov 2026: 22 presses → 22 counts.
