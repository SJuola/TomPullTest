

const uint8_t bufferSize = 5;
uint8_t buffer[bufferSize];

void setup() {
  Serial.begin(115200);
}

void loop() {
  Serial.println("Ready");
  if( Serial.available())
  {
    char cmd = Serial.read();
  }
}

uint8_t checksum(){
  uint8_t result = 0;
  uint16_t sum = 0;
  
  for(uint8_t i = 0; i < (bufferSize - 1); i++)
  {
    sum += buffer[i];
  }
  result = sum & 0xFF;

  return result;
}
