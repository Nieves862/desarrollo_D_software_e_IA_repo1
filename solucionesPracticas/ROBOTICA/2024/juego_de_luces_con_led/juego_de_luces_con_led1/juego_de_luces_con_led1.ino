void blink (int pin, int msek){
digitalWrite (pin, HIGH);
delay (msek);
digitalWrite (pin, LOW);
delay (msek);
}

void setup() {
  // put your setup code here, to run once:
  pinMode(8,OUTPUT);
  pinMode(9,OUTPUT);
  pinMode(10,OUTPUT);
  pinMode(11,OUTPUT);
  pinMode(12,OUTPUT);  
}

void loop() {
  // Parpadeo
blink (8,1000); //Dauer in Millisekunden
blink (9,1000);
blink (10,1000);
blink (11,1000);
blink (12,1000);
}
