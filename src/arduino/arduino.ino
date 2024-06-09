void setup() {
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT); // Comunicación con el ordenador
  delay(1000);
}

void loop() {
  if (Serial.available() > 0) {
    String msg = Serial.readString();
    Serial.println(msg);

    if (msg) {
      digitalWrite(LED_BUILTIN, HIGH);
    }
  }
}
