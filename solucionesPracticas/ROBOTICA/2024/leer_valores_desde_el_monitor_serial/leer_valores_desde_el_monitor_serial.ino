int myNumber;
String msg1 = "Por Favor Ingresa el Número que te GUSTE:";
String msg2 = "Tu Número es: ";

void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
Serial.println(msg1);
while (Serial.available() == 0){ 

}
myNumber = Serial.parseInt();
Serial.print(msg2);
Serial.println(myNumber);
}
