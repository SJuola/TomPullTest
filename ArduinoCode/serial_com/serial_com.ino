const uint8_t bufferSize = 5;
uint8_t buffer[bufferSize];

bool SERIAL_TEST_FLAG = true;
#define MOTOR1 1
#define MOTOR2 2

void setup() {
  Serial.begin(115200);
  pinMode(MOTOR1, OUTPUT);
  pinMode(MOTOR2, OUTPUT);
  //handshake();
}

void loop() {
  if(Serial.available())
  {
    Serial.println("Echo back " + Serial.read());
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

void setup_encoder()
{
  /*Use pin 2 and 3 for channel A and B of the encoder respectively*/
  pinMode(2,INPUT_PULLUP);
  pinMode(3,INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(2), read_encoder, CHANGE);
  attachInterrupt(digitalPinToInterrupt(3), read_encoder, CHANGE);
}

int read_encoder()
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
