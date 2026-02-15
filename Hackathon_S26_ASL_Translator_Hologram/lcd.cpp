

// include the library code:
#include <Arduino.h>
#include <LiquidCrystal.h>
#include <string>


// initialize the library by associating any needed LCD interface pin
// with the arduino pin number it is connected to
const int rs = D5, en = D4, d4 = D3, d5 = D2, d6 = D1, d7 = D0;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);

void lcd_init(void) {
  // set up the LCD's number of columns and rows:
  lcd.begin(16, 2);
}

void lcd_set_text(String str) {
  lcd.clear();
  lcd.setCursor(0, 0);
  //replace(str, '_', ' ');
  if (str.length() <= 16) {
    lcd.print(str);
  } else {
    lcd.print(str.substring(0, 16));
    lcd.setCursor(0, 1);
    lcd.print(str.substring(16, str.length()));
  }
}