unsigned long previousMillis = 0;
const long interval = 10;
unsigned int SerialBuffer = 0;
int TX_data[4];
#define RY01_pin  3
#define RY02_pin  4
#define Temp1_pin A0
#define Temp2_pin A1
#define Soil1_pin A2
#define Soil2_pin A3
#define ON  0
#define OFF 1
void setup() {
  Serial.begin(9600);
  pinMode(RY01_pin, OUTPUT);
  pinMode(RY02_pin, OUTPUT);
  pinMode(Temp1_pin, INPUT);
  pinMode(Temp2_pin, INPUT);
  pinMode(Soil1_pin, INPUT);
  pinMode(Soil2_pin, INPUT);
  digitalWrite(RY01_pin, OFF);
  digitalWrite(RY02_pin, OFF);
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
    case 'B':
      digitalWrite(RY02_pin, ON);
      break;
    case 'b':
      digitalWrite(RY02_pin, OFF);
      break;
  }

  TX_data[0] = analogRead(Temp1_pin);
  TX_data[1] = analogRead(Temp2_pin);
  TX_data[2] = analogRead(Soil1_pin);
  TX_data[3] = analogRead(Soil2_pin);

  TX_data[0] = map(TX_data[0],0,1024,0,100);
  TX_data[1] = map(TX_data[1],0,1024,0,100);
  TX_data[2] = map(TX_data[2],0,1024,0,100);
  TX_data[3] = map(TX_data[3],0,1024,0,100);

  //Serial.println(String(Value[0])+","+String(Value[1])+","+String(Value[2])+","+String(Value[3]));
  unsigned long currentMillis = millis();
  if (currentMillis - previousMillis >= interval) {
    previousMillis = currentMillis;
    Serial.println(String(TX_data[0])+","+String(TX_data[1])+","+String(TX_data[2])+","+String(TX_data[3]));
  }
}