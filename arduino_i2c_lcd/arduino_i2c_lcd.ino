#include <LiquidCrystal_I2C.h>


  LiquidCrystal_I2C lcd(0x27, 16, 2);
void setup() {
  // put your setup code here, to run once:
  lcd.init();
  lcd.backlight();
  Serial.begin(115200);
}

byte inByte = 0;
void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available() > 0) {
    inByte = Serial.read();
    lcd.setCursor(0, 0);
    if (inByte != 10) {
        
      lcd.write(inByte);
      Serial.print("Recieved: ");
      Serial.println(inByte);
    }
    lcd.flush();
  }
  //delay(500);
}
