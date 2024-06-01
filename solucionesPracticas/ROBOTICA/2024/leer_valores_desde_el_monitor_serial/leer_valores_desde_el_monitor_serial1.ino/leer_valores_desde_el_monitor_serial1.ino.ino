//int ledPin = 8;
//int blinkTimes;
//String msg1 = "Por favor ingresa el número de parpadeos: ";
//int i;
//int dt = 300;
//
//void setup() {
//  // put your setup code here, to run once:
//  Serial.begin(9600);
//  pinMode(ledPin,OUTPUT);
//}
//
//void loop() {
//  // put your main code here, to run repeatedly:
//  Serial.println();
//  Serial.println(msg1);
//  while (Serial.available() == 0) {
//
//  }
//  blinkTimes = Serial.parseInt();
//
//  for (i = 1; i <= blinkTimes; i++) { //i = i + 1
//    digitalWrite(ledPin, HIGH);
//    delay(dt);
//    digitalWrite(ledPin, LOW);
//    delay(dt);
//  }
//}
