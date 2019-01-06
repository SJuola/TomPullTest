#include <math.h>

#define channelA 2
#define channelB 3
#define numOfSteps 20

volatile int stateA = LOW; //store the current state of channel A
volatile int stateB = LOW;
volatile int counter = 0;
volatile long startTime = millis();

void setup() {
  pinMode(channelA, INPUT_PULLUP);
  pinMode(channelB, INPUT_PULLUP);
  pinMode(LED_BUILTIN, OUTPUT);

  attachInterrupt(digitalPinToInterrupt(channelA), read_encoderA, CHANGE);
  attachInterrupt(digitalPinToInterrupt(channelB), read_encoderB, CHANGE);

  stateA = digitalRead(channelA);
  stateB = digitalRead(channelB); //initial reading of each channel
  
  Serial.begin(9600);
}

void loop() {
  if( Serial.available())
  {
    //blink();
    Serial.println(Serial.readString());
  }
}
void blink()
{
  for( int i=0; i<20; i++)
  {
    digitalWrite(LED_BUILTIN, HIGH);
    delay(30);
    digitalWrite(LED_BUILTIN, LOW);
    delay(30);
  }
}
void read_encoderA()
{
  stateA = !stateA; //switch state
  if( stateA==HIGH) // Incoming edge
  {
    const String result = "RPM: ";
    float rpm = calRPM();
    Serial.println(result + rpm);
    if(stateB==LOW) //Channel A is leading channel B
    {
      counter++;
      if( counter==numOfSteps)
      counter =  (counter==numOfSteps) ? 0 : counter;
    }
    else
    {
      counter--;
      counter = (counter==-1) ? numOfSteps-1 : counter;
    }
    Serial.println(counter);
  }
}

void read_encoderB()
{
  stateB = !stateB;
}

float calRPM()
{
  long curTime = millis();
  int deltaTime = millis() - startTime;
  startTime = curTime;
  return ((1/numOfSteps)/(deltaTime*0.000001/60.0));
}
