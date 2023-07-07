//adapted from https://www.electroniclinic.com/arduino-dc-motor-speed-control-with-encoder-arduino-dc-motor-encoder/
//adapted from https://dronebotworkshop.com/tb6612fng-h-bridge/
#include <SparkFun_TB6612.h>
//===MOTOR DRIVER===//
//board 1 A side
#define PWMA 11
#define AIN1 12
#define AIN2 13
#define STBY 14 //needs 5V; set to digitalWrite(HIGH), it works!
Motor motor1 = Motor(AIN1,AIN2,PWMA,1,STBY);
//board 1 B side
#define PWMB 15
#define BIN1 16
#define BIN2 17
Motor motor2 = Motor(BIN1,BIN2,PWMB,1,STBY);
//board 2 C side
#define C_PWMA 22
#define C_AIN1 23
#define C_AIN2 24
#define C_STBY 25 //needs 5V; set to digitalWrite(HIGH), it works!
Motor motor3 = Motor(C_AIN1,C_AIN2,C_PWMA,1,C_STBY);
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
//motor 3
#define ENC_VCC_3 32 //needs 5V; set to digitalWrite(HIGH), it works!
#define ENCA_3 20
#define ENCB_3 21
int Count_pulses_3 = 0; //for encoders
void setup()
{
  Serial.begin(9600);
  //===MOTOR DRIVER===//
  //board 1 A side
  pinMode(STBY,OUTPUT); //get pin to deliver 5V to standby
  digitalWrite(STBY, HIGH);
  //board 2 C side
  pinMode(C_STBY,OUTPUT);
  digitalWrite(C_STBY, HIGH);
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
  //motor 3
  pinMode(ENCA_3,INPUT); // sets the encoder A pin as the input
  pinMode(ENCB_3,INPUT); // sets the encoder B pin as the input
  pinMode(ENC_VCC_3,OUTPUT); //get pin to deliver 5V to encoder
  digitalWrite(ENC_VCC_3, HIGH);
  attachInterrupt(digitalPinToInterrupt(ENCA_3),DC_Motor_Encoder_3,RISING); 
}
void loop() 
{
  //encoder print pulses (position relative to start)
  Serial.println("Motor1: " +Count_pulses_1);
  Serial.println("Motor2: " +Count_pulses_2);
  Serial.println("Motor3: " +Count_pulses_3);
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
void DC_Motor_Encoder_3() //used for encoders, don't delete
{
  int b3 = digitalRead(ENCB_3);
  if(b3 > 0)
    {
      Count_pulses_3++;
    }
  else
    {
      Count_pulses_3--;
    }
}