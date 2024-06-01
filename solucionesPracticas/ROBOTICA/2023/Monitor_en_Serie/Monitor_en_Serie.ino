
int i = 0;
int wait = 500;
int x = 10;
int y = 8;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:
int z = x + y;
  //Serial.print("x");
  //Serial.print("+");
  //Serial.print("y");
  //Serial.print("=");
  Serial.print(" x + y= ");
  Serial.println(z);
  delay(wait);
  i=i+1;

  

}
