unsigned int SerialBuffer = 0;
#define RY01_pin  3
#define ON  0
#define OFF 1
void setup() {
  Serial.begin(9600);
  pinMode(RY01_pin, OUTPUT);
  digitalWrite(RY01_pin, OFF);
}

void loop() {
  if(Serial.available()){
    SerialBuffer = Serial.read();
  }
  switch(SerialBuffer){
    case 'A':
      digitalWrite(RY01_pin, ON);
      break;
    case 'a':
      digitalWrite(RY01_pin, OFF);
      break;
  }
}
