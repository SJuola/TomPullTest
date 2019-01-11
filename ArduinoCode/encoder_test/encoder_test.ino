#include <math.h>

#define channelA 2     // Use pin 2 and 3 for reading encoder
#define channelB 3

#define motorChanA 4   // User pin 4 and 5 to control stepper motor
#define motorChanB 5
#define numOfSteps 200 // Num of steps for 1 rev of the stepper motor
#define debug true     // For debugging purposes

volatile int stateA = LOW; //store the current state of channel A
volatile int stateB = LOW;
volatile unsigned long counter = 0;
volatile unsigned long startTime = millis();

//Serial com variables
String cmdString   = "";
String paramString = "";

bool cmdReadComplete    = false;
bool paramReadComplete  = false;
bool stringComplete     = false;
bool estop_flag         = false;


//Timing
unsigned long prevTime = millis();

void setup() {
  pinMode(channelA, INPUT_PULLUP);
  pinMode(channelB, INPUT_PULLUP);
  pinMode(motorChanA, OUTPUT);
  pinMode(motorChanB, OUTPUT);
  pinMode(LED_BUILTIN, OUTPUT);

  attachInterrupt(digitalPinToInterrupt(channelA), read_encoderA, CHANGE); //Use CHANGE for higher resolution
  attachInterrupt(digitalPinToInterrupt(channelB), read_encoderB, CHANGE);
  stateA = digitalRead(channelA);
  stateB = digitalRead(channelB); //initial reading of each channel
  Serial.begin(115200);
}

void loop() {
  if(stringComplete)
  {
    String paramVal = paramString.substring(1, paramString.length());
    if(cmdString.equals("spin"))
    {
      for(int i=0; i<50000; i++)
      {
        if(!estop_flag)
        {
          spinOnce(paramVal.toInt());  
        }
        else
        {
          spinStop();
          break;
        }
      } 
    }
    else if(cmdString.equals("spinStop"))
    {
      estop_flag = true;
    }
    else if(cmdString.equals("jogStart"))
    {
      jogMode(true);
    }
    else if(cmdString.equals("jogStop"))
    {
      jogMode(false);
    }
    else
    {
      Serial.println("Unrecognized commands");
    }

    stringComplete = false; //reset flag
    cmdString = "";       //reset input string
    paramString = "";
    cmdReadComplete = false;
    paramReadComplete = false;
  }
}



/* Serial event is triggered when there is data in the 
 *  serial buffer
 *  Serial data format:
 *  command:parametervalue\n
 */
void serialEvent() {
  while (Serial.available())
  {
    char inChar = (char)Serial.read();
    
    if (inChar == ':') 
    {
      cmdReadComplete = true;
    }
    
    if(inChar =='\n')
    {
      stringComplete = true;
      paramReadComplete = true;
    }

    if(!cmdReadComplete)
    {
      cmdString += inChar;
    }
    
    if(cmdReadComplete && !paramReadComplete)
    {
      paramString += inChar;
    }
  }
}

/* Motor will spin continuously
 */
void spinOnce(int wait)
{
  digitalWrite(motorChanA,HIGH);
  digitalWrite(motorChanB,LOW);
  delayMicroseconds(wait);
  digitalWrite(motorChanA,LOW);
  digitalWrite(motorChanB,HIGH);
  delayMicroseconds(wait);
}

void spinStop()
{
  digitalWrite(motorChanA,LOW);
  digitalWrite(motorChanB,LOW);
}

void jogMode(bool enable)
{
  if(enable)
  {
    digitalWrite(motorChanA,HIGH);
    digitalWrite(motorChanB,LOW);
    delayMicroseconds(200);
    digitalWrite(motorChanB,HIGH);
    digitalWrite(motorChanA,LOW);
    delayMicroseconds(200);
  }
  else
  {
    digitalWrite(motorChanA, LOW);
    digitalWrite(motorChanB, LOW);
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
    if(stateB==LOW) //Channel A is leading channel B
    {
      counter++;
      if( counter==numOfSteps)
      {
        Serial.println(calcRPM());
        counter = 0;
      }
    }
    else
    {
      counter--;
      if( counter==-1)
      {
        Serial.println(calcRPM());
        counter = numOfSteps-1;
      }
    }
    if(debug)
    {
      String out = "counter: ";
      Serial.println(out + counter);
    }
  }
}

void read_encoderB()
{
  stateB = !stateB;
}

unsigned int calcRPM()
{
  unsigned long curTime = millis();
  unsigned int deltaTime = millis() - startTime;
  startTime = curTime;
  return ((1/numOfSteps)/(deltaTime*0.000001/60.0));
}
