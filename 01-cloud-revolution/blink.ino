void setup() {
  pinMode(2, OUTPUT);
}
void loop() {
  digitalWrite(2, HIGH);  // LED on
  delay(500);
  digitalWrite(2, LOW);   // LED off
  delay(500);
}
