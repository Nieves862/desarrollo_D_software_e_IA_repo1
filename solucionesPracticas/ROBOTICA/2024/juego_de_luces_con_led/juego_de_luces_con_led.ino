int pin1= 8;
int pin2= 9;
int pin3= 10;
int pin4= 11;
int pin5= 12;


void setup() {
  // put your setup code here, to run once:
  pinMode(pin1,OUTPUT);
  pinMode(pin2,OUTPUT);
  pinMode(pin3,OUTPUT);
  pinMode(pin4,OUTPUT);
  pinMode(pin5,OUTPUT);  

}

void loop() {
  // Parpadeo del Pin 1
  digitalWrite(pin1,HIGH);
  delay(100);
  digitalWrite(pin1,LOW);
  delay(100);

  //Pin 2
  digitalWrite(pin2,HIGH);
  delay(100);
  digitalWrite(pin2,LOW);
  delay(100);

  //Pin 3
  digitalWrite(pin3,HIGH);
  delay(100);
  digitalWrite(pin3,LOW);
  delay(100);

  //Pin 4
  digitalWrite(pin4,HIGH);
  delay(100);
  digitalWrite(pin4,LOW);
  delay(100);

  //Pin 5
  digitalWrite(pin5,HIGH);
  delay(100);
  digitalWrite(pin5,LOW);
  delay(100);
}
