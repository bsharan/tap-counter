const int BUTTON = 4;      // button on pin 4 (right column)
const int LED = 2;         // LED on pin 2 (right column)
int count = 0;             // number of sales tapped today
bool wasPressed = false;   // MEMORY: was the button down last time we checked?

void setup() {
  pinMode(BUTTON, INPUT_PULLUP);   // reads HIGH normally, LOW when pressed
  pinMode(LED, OUTPUT);
  Serial.begin(115200);            // lets the board print text to the screen
  Serial.println("Tap-Counter ready");
}

void loop() {
  bool pressed = digitalRead(BUTTON) == LOW;
  if (pressed && !wasPressed) {    // only the MOMENT it goes down = one sale
    count++;
    Serial.print("Sale! Count = ");
    Serial.println(count);
    digitalWrite(LED, HIGH);       // "sale recorded" light
    delay(150);
    digitalWrite(LED, LOW);
  }
  wasPressed = pressed;            // remember for next time
  delay(20);                       // ignore tiny electrical bounces
}
