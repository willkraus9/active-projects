//adapted from https://www.electroniclinic.com/arduino-dc-motor-speed-control-with-encoder-arduino-dc-motor-encoder/
//adapted from https://dronebotworkshop.com/tb6612fng-h-bridge/
#include <SparkFun_TB6612.h>
//===MOTOR DRIVER===//
//board 1 A side
#define A_PWMA 11
#define A_AIN1 12
#define A_AIN2 13
#define AB_STBY 14 //needs 5V; set to digitalWrite(HIGH), it works!
Motor motor1 = Motor(A_AIN1,A_AIN2,A_PWMA,1,AB_STBY);
//board 1 B side
#define B_PWMB 15
#define B_BIN1 16
#define B_BIN2 17
Motor motor2 = Motor(B_BIN1,B_BIN2,B_PWMB,1,AB_STBY);
//board 2 C side
#define C_PWMA 22
#define C_AIN1 23
#define C_AIN2 24
#define CD_STBY 25 //needs 5V; set to digitalWrite(HIGH), it works!
Motor motor3 = Motor(C_AIN1,C_AIN2,C_PWMA,1,CD_STBY);
//board 2 D side
#define D_PWMA 26
#define D_AIN1 27
#define D_AIN2 28
#define CD_STBY 29 //needs 5V; set to digitalWrite(HIGH), it works!
Motor motor4 = Motor(D_AIN1,D_AIN2,D_PWMA,1,CD_STBY);
//===MOTOR ENCODER===//
//motor 1
#define ENC_VCC_1 30 //needs 5V; set to digitalWrite(HIGH), it works!
#define ENCA_1 2
#define ENCB_1 3
int Count_pulses_1 = 0; //for encoders
//motor 2
#define ENC_VCC_2 31 //needs 5V; set to digitalWrite(HIGH), it works!
#define ENCA_2 18
#define ENCB_2 19
int Count_pulses_2 = 0; //for encoders
void setup()
{
  Serial.begin(9600);
  //===MOTOR DRIVER===//
  //board 1 A side
  pinMode(AB_STBY,OUTPUT); //get pin to deliver 5V to standby
  digitalWrite(AB_STBY, HIGH);
  //board 2 C side
  pinMode(CD_STBY,OUTPUT);
  digitalWrite(CD_STBY, HIGH);
  //===MOTOR ENCODER===//
  //motor 1
  pinMode(ENCA_1,INPUT); // sets the encoder A pin as the input
  pinMode(ENCB_1,INPUT); // sets the encoder B pin as the input
  pinMode(ENC_VCC_1,OUTPUT); //get pin to deliver 5V to encoder
  digitalWrite(ENC_VCC_1, HIGH);
  attachInterrupt(digitalPinToInterrupt(ENCA_1),DC_Motor_Encoder_1,RISING); 
  //motor 2
  pinMode(ENCA_2,INPUT); // sets the encoder A pin as the input
  pinMode(ENCB_2,INPUT); // sets the encoder B pin as the input
  pinMode(ENC_VCC_2,OUTPUT); //get pin to deliver 5V to encoder
  digitalWrite(ENC_VCC_2, HIGH);
  attachInterrupt(digitalPinToInterrupt(ENCA_2),DC_Motor_Encoder_2,RISING); 
}
void loop() 
{
  //encoder print pulses (position relative to start)
  Serial.println("Motor1: " +Count_pulses_1);
  Serial.println("Motor2: " +Count_pulses_2);
  //go forward
  Serial.println("Forward");
  motor1.drive(255,1000);
  motor1.drive(-255,1000);
  motor1.brake();
  delay(1000);
  //go backward
  Serial.println("Backward");
  motor1.drive(-255,1000);
  motor1.drive(255,1000);
  motor1.brake();
  delay(1000);  
}
void DC_Motor_Encoder_1() //used for encoders, don't delete
{
  int b1 = digitalRead(ENCB_1);
  if(b1 > 0)
    {
      Count_pulses_1++;
    }
  else
    {
      Count_pulses_1--;
    }
}
void DC_Motor_Encoder_2() //used for encoders, don't delete
{
  int b2 = digitalRead(ENCB_2);
  if(b2 > 0)
    {
      Count_pulses_2++;
    }
  else
    {
      Count_pulses_2--;
    }
}