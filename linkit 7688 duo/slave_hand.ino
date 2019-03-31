#include <SoftwareSerial.h>
#include "I2Cdev.h"
#include "MPU6050.h"
SoftwareSerial BTSerial(10, 11);

char val;  
String recieveData = "";   
bool startRecieve = false;  
void setup()  
{  
  
  pinMode(3,OUTPUT);  //in hand_control_mode
  pinMode(4,OUTPUT);  //music_control, stop
  pinMode(5,OUTPUT);  //music_control
  pinMode(6,INPUT);   //is light_mode
  pinMode(7,INPUT);   //is music_mode
  pinMode(9,OUTPUT);  //LED pin
  pinMode(12,OUTPUT); //music_control
  Serial.begin(38400);   
  BTSerial.begin(9600); //HC-06 預設 baud
  digitalWrite(3,LOW);
  digitalWrite(4,LOW);
  digitalWrite(5,LOW);
  digitalWrite(9,LOW);
  digitalWrite(12,LOW);
}  
int light_mode = 0;
int music_mode = 0;
void loop()  
{  
    Serial.print(digitalRead(6));
    Serial.print(light_mode);
    Serial.print(digitalRead(7));
    Serial.println(music_mode);
    //Serial.println(1);
    //startRecieve = true;  
    if (light_mode==0 && music_mode==0 && digitalRead(6)){
      light_mode=1;
      digitalWrite(3,HIGH);
    }
    else if (light_mode==0 && music_mode==0 && digitalRead(7)){
      music_mode=1;
      digitalWrite(3,HIGH);
    }
    if (light_mode==1 && music_mode==1){
      light_mode=0;
      music_mode=0;
    }
    
    //Serial.println(digitalRead(7));
    //Serial.println(mode);
    while(BTSerial.available()) //如果有收到資料  
    {  
      val = BTSerial.read(); //每次接收一個字元
      Serial.println(val);
      if (light_mode==1 && music_mode==0){
        if (val=='f'){
          analogWrite(9, 0);
        }
        else if (val=='x'){
          analogWrite(9, 85);
        }
        else if (val=='y'){
          analogWrite(9, 180);
        }
        else if (val=='z'){
          analogWrite(9, 255);
        }
        else if (val=='N'){
          light_mode = 0;
          digitalWrite(3,LOW);
          delay(250);
          break;
        }
        else if (val=='T'){
          light_mode = 0;
          analogWrite(9, 0);
          digitalWrite(3,LOW);
          delay(250);
          break;
        }
      }
      else if (light_mode==0 && music_mode==1){
        if (val=='f'){
          digitalWrite(4,LOW);
          digitalWrite(5,LOW);
          digitalWrite(12,LOW);
        }
        else if (val=='x'){
          digitalWrite(4,LOW);
          digitalWrite(5,LOW);
          digitalWrite(12,HIGH);
        }
        else if (val=='y'){
          digitalWrite(4,LOW);
          digitalWrite(5,HIGH);
          digitalWrite(12,LOW);
        }
        else if (val=='z'){
          digitalWrite(4,LOW);
          digitalWrite(5,HIGH);
          digitalWrite(12,HIGH);
        }
        else if (val=='N'){
          music_mode = 0;
          digitalWrite(3,LOW);
          digitalWrite(4,LOW);
          digitalWrite(5,LOW);
          digitalWrite(12,LOW);
          delay(250);
          //music_mode = 0;
          break;
        }
        else if (val=='T'){
          music_mode = 0;
          digitalWrite(3,LOW);
          digitalWrite(4,HIGH);
          digitalWrite(5,LOW);
          digitalWrite(12,LOW);
          delay(250);
          digitalWrite(4,LOW);
          break;
        }
    }
    //recieveData += val; //字元組成字串  
    //BTSerial.write(byte(val)); //把每次收到的字元轉成byte封包傳至手機端  
    //delay(1000);  //每次傳輸間隔，如果太短會造成資料遺失或亂碼  
    }  
}
  /*if(startRecieve)  
  {  
  startRecieve = false;  
  Serial.println(recieveData); //呈現收到字串  
  recieveData = "";  
  }  
    delay(300);  
}  */
/*int16_t ax, ay, az;
int16_t gx, gy, gz;
#define MAX_STRING 128
char cmd[MAX_STRING];               // var: Received command from Android
int cmd_len = 0;                    // var: Received command length record

void setup() {
  // put your setup code here, to run once:
    Serial.begin(38400);             // Init: Arduino <-> Computer Baud Rate
    BTSerial.begin(9600);           // Init: HC-05 <-> Arduino Baud Rate
}

void loop() {
    // put your main code here, to run repeatedly:
    int tick = 0;
    int i = 0;
    int cmd_tmp_size = 0;
    char str[128];
    char chr;
    char data[128];
  //  Serial.print(BTSerial.read());
    if () {
        // 讀取傳入的字元值
        while ((chr = char(BTSerial.read())) != '\n') {
            // 確認輸入的字元介於'0'和'9'，且索引i小於3（確保僅讀取前三個字）     
            data[i] = chr;
            i++;
        }
        Serial.println(5);
    }
    //Serial.println(data[0]);
    //Serial.println(data[1]);
    //Serial.println(data[2]);
    /*//*/Serial.println(ax);
    while ( tick < 128 ){
        cmd_tmp_size = BTSerial.available();        // Get the size of commands waiting to be read
        if (cmd_tmp_size!=0){
            Serial.println(cmd_tmp_size);
        }
        if ( cmd_tmp_size > 0 ){                    // If there are commands waiting
            for ( i=0; i < cmd_tmp_size; i++ ){     // For each command character waiting
                cmd[(cmd_len++)%MAX_STRING] = char(BTSerial.read());
                                                    // Read command character and save it into cmd
            }
        }
        else {
            tick++;
        }
    }
    if (cmd_len){                   // If cmd have content
        sprintf(str,"%s",cmd);      // Convert cmd to string, and print formatted string to str
        Serial.println(str[0]);     // Print str by Serial
        cmd[0] = '\0';              // Clean cmd
    }
    cmd_len = 0;                    // Reset cmd's length record
*/
    
//}
