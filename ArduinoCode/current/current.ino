#include <IoAbstraction.h>
#include <CommandHandler.h>
#include <MegunoLink.h>
#include <AccelStepper.h>
#include <ArduinoTimer.h>

/* IO Abstraction: Library for event-based programming instead of using loops
 * - API/tutorial: https://www.thecoderscorner.com/products/arduino-libraries/io-abstraction/
 * 
 * AccelStepper: Library to drive a stepper motor
 * - API/tutorial: https://www.airspayce.com/mikem/arduino/AccelStepper/classAccelStepper.html
 * 
 * CommandHandler: Library to receive serial command from a computer
 * and assign a callback function to be call when associative serial commands are received.
 *  - Tutorial: https://www.megunolink.com/documentation/arduino-libraries/serial-command-handler/
 */

#define debug true // Allow printing out useful information for debugging purposes
#define motorPin    4
#define distanceSensor A0v //Good distance sensor for this application: https://www.amazon.com/gp/product/B00IMOSEJA/ref=crt_ewc_title_srh_1?ie=UTF8&psc=1&smid=A1G08I38URAWZJ
AccelStepper stepper(AccelStepper::DRIVER, motorPin);
const int    accel        = 10000; 
const int    maximumSpeed = 20000;
const byte   numRot       = 2;
const int    stepsPerRot  = 400;
unsigned int speed        = 50;

CommandHandler<> SerialCommandHandler;
TimePlot plt;
ArduinoTimer timer1;

byte motorState                = LOW;
byte LED_STATE                 = LOW;
volatile unsigned long counter = 0;

// Flags
bool estop_flag         = false;

//Task IDs
uint8_t sendingData_task;
uint8_t motorControl_task;

IoAbstractionRef arduinoPins = ioUsingArduino();

/*  OBSOLETE
 *  Description: Function to move the motor ONE step
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

/* Description: Function to call when receive command to start
 * the test via serial
 */
void start_test_callback(CommandParameter &param)
{
  Serial.println("Test started");
  motorControl_task = taskManager.scheduleOnce(0, []{
        stepper.runToNewPosition(numRot*stepsPerRot);
  });
}

void stop_test_callback()
{
  taskManager.cancelTask(motorControl_task);
}

//void blink(CommandParameter &param)
void blinkOnce()
{
  digitalWrite(4, LED_STATE);
  LED_STATE = !LED_STATE;
}
void sendSpeedData_callback()
{
  plt.SendData("", analogRead(A0)); //Example of sending data from an anlog pin
}

void setup() 
{
  Serial.begin(115200);

  pinMode(4, OUTPUT);

  /******** Serial command setup using CommandHandler library****/
  SerialCommandHandler.AddCommand(F("START_TEST"), start_test_callback);
  SerialCommandHandler.AddCommand(F("STOP_TEST"), stop_test_callback);
  //SerialCommandHandler.AddCommand(F("BLINK"), blink_callback);            // Serial command to blink Arduino built-in LED
  SerialCommandHandler.AddCommand(F("BLINK"), [](CommandParameter &param){
    if(debug)
    {
      Serial.println("Start to blink.");
    }
    sendingData_task = taskManager.scheduleFixedRate( speed, blinkOnce);
  });
  SerialCommandHandler.AddCommand(F("STOP_BLINK"), [](CommandParameter &param){
    if(debug)
    {
      Serial.println("Stop blinking ...");
      digitalWrite(4, LOW); //make sure the LED is off
    }
    taskManager.cancelTask(sendingData_task);
    });
  SerialCommandHandler.AddVariable(F("SET_SPEED"), speed);                // e.g. Serial command: !SET_SPEED 100 will set the speed variable to 100

  /******** Sending speed values to Computer via serial using MegunoLink TimePlot library*/
  //taskManager.scheduleFixedRate(10, sendSpeedData_callback, TIME_MICROS);
  
  /******** Stepper setup using StepperAccel library ***********/
  stepper.setMaxSpeed(maximumSpeed);
  stepper.setSpeed(speed);
  stepper.setAcceleration(accel);
}

void loop() {
  taskManager.runLoop();
  SerialCommandHandler.Process();
}
