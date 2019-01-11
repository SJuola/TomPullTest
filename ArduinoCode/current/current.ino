#include<IoAbstraction.h>
#include <AccelStepper.h>

/* IO Abstraction: Library for event-based programming instead of using loops
 * - API/tutorial: https://www.thecoderscorner.com/products/arduino-libraries/io-abstraction/
 * 
 * AccelStepper: Library to drive a stepper motor
 * - API/tutorial: https://www.airspayce.com/mikem/arduino/AccelStepper/classAccelStepper.html
 */

#define encoderAPin 2       // Use pin 2 and 3 for reading encoder
#define encoderBPin 3
#define maximumEncoderVal 128

#define motorPin    4
#define debug       true     // For debugging purposes

AccelStepper stepper(AccelStepper::DRIVER, motorPin);
const byte numRot      = 2;
const int stepsPerRot = 400;

volatile int motorState        = LOW;
volatile unsigned long counter = 0;


//Serial com variables
String cmdString   = "";
String paramString = "";

// Flags
bool cmdReadComplete    = false;
bool paramReadComplete  = false;
bool stringComplete     = false;
bool estop_flag         = false;

//Task IDs
uint8_t serialCom_task;
uint8_t motorControl_task;

//Time
unsigned long prevTime;

IoAbstractionRef arduinoPins = ioUsingArduino();


/* Function to check the serial port for commands coming from
 * the GUI
 * Serial data format: command:parameter\n
 */
void serialData_callback()
{
  while(Serial.available()>0)
  {
    char inChar = (char)Serial.read();
    
    if (inChar == ':') //Done getting the type of command from serial data
    {
      cmdReadComplete = true;
    }
    
    if(inChar =='\n') //Done parsing the whole serial data
    {
      stringComplete    = true;
      paramReadComplete = true;
      prevTime = millis();
      //motorControl_task = taskManager.scheduleFixedRate(paramString.toInt(), spinOnce, TIME_MICROS); //move the motor at the specified micros delay
      motorControl_task = taskManager.scheduleOnce(0, []{
        stepper.runToNewPosition(numRot*stepsPerRot);
      });
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


/* Function to move the motor one step
 */
void spinOnce()
{
  ioDeviceDigitalWriteS(arduinoPins,motorPin,motorState);
  motorState = !motorState;
  counter++;

  /*Test using counter to stop the motor*/
  if(counter >= 10000)
  {
    taskManager.cancelTask(motorControl_task);
    counter = 0;
  }
}

void setup() {
  Serial.begin(115200);

  /******** Encoder setup ********/
  // First we set up the switches library, giving it the task manager and tell it to use arduino pins
  // We could also of chosen IO through an i2c device that supports interrupts.
  // If you want to use PULL UP instead of PULL DOWN logic, uncomment the additional parameter below
  switches.initialise(ioUsingArduino());

  // now we set up the rotary encoder, first we give the A pin and the B pin.
  // we give the encoder a max value of 128 (i.e. maxiumumEncoderVal), always minumum of 0.
  setupRotaryEncoderWithInterrupt(encoderAPin, encoderBPin, [](int val){
      Serial.println(val);
  });
  switches.changeEncoderPrecision(maximumEncoderVal, 100);

  /******** Setup serial communication ********/
  // Checking on the serial every 5 microseconds
  ioDevicePinMode(arduinoPins, motorPin, OUTPUT);
  taskManager.scheduleFixedRate(5, serialData_callback, TIME_MICROS); // timerUnit is one of enum TimerUnit TIME_MICROS, TIME_SECONDS, TIME_MILLIS

  /******** Stepper setup ***********/
  stepper.setMaxSpeed(20000);
  stepper.setSpeed(5000);
  stepper.setAcceleration(10000);
}

void loop() {
  taskManager.runLoop();
}
