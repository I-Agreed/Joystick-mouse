float x;
float y;

void setup() {
  Serial.begin(9600);
  

}

void loop() {
  x = analogRead(5);
  x -= 512.5;
  x /= 512.5;
  
  y = analogRead(4);
  y -= 512.5;
  y /= 512.5;
  Serial.print("|");
  Serial.print(x);
  Serial.print(", ");
  Serial.print(y);
  

}
