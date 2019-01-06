const uint8_t bufferSize = 5;
uint8_t buffer[bufferSize];

bool SERIAL_TEST_FLAG = true;
#define MOTOR1 1
#define MOTOR2 2

void setup() {
  Serial.begin(2000000);
  pinMode(MOTOR1, OUTPUT);
  pinMode(MOTOR2, OUTPUT);
  handshake();
}

void loop() {
  if( Serial.available()>0)
  {
    if( SERIAL_TEST_FLAG)
    {
      Serial.println("Ready");
    }
    Serial.println(Serial.read());//send back to the sender
  }
}
void handshake()
{
  while(Serial.available()<=0)
  {
    Serial.println("Waiting for commands ...");
    delay(100);
  }
}
void accelerate_ramp(double acceleration_time)
{
  
}

/*Checksum to verify data content sent through serial port*/
uint8_t checksum()
{
  uint8_t result = 0;
  uint16_t sum = 0;
  
  for(uint8_t i = 0; i < (bufferSize - 1); i++)
  {
    sum += buffer[i];
  }
  result = sum & 0xFF;

  return result;
}
