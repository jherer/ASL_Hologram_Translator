#include <Arduino.h>
#include <ESP8266WiFi.h>
#include <Hash.h>
#include <ESPAsyncTCP.h>
#include <ESPAsyncWebServer.h>
#include "lcd.hpp"


const char* ssid     = "ESP8266-Access-Point-PLSAFN82";
const char* password = "12345678374";

IPAddress local_IP(192,168,4,22);
IPAddress gateway(192,168,4,9);
IPAddress subnet(255,255,255,0);

AsyncWebServer server(80);

int seconds_elapsed = 0;

const char index_html[] PROGMEM = R"rawliteral(
<!DOCTYPE HTML>
<html>
<head>
  <title>ESP8266 Server</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body>
  <h2>ESP8266 Server</h2>
  <form method="POST" action="javascript:submitForm()">
  <input type="text" name="msg" id="msg">
  <input type="submit" name="submit" id="btn" value="Send">
  </form>
  <p id="sentmsg">Nothing sent yet</p>
</body>
<script>
  var msg;
  function submitForm() {
    var xhr = new XMLHttpRequest();
    msg = document.getElementById("msg").value;
    xhr.open("GET", "/send?msg=" + msg);
    xhr.send();
    document.getElementById("sentmsg").innerHTML = "Sent: &quot;" + msg + "&quot;";
  }
</script>
</html>)rawliteral";

String s;
bool recieved = false;
void handleForm(AsyncWebServerRequest *request) {
  if (request->hasParam("msg")) {
    recieved = true;
    s = request->getParam("msg")->value();
    request->send(200, "text/html", "OK");
    Serial.print("String recieved: ");
    Serial.println(s);
  } else {
    recieved = false;
    request->send(200, "text/html", "NOT recieved");
    Serial.println("String NOT recieved");
  }
}




void setup(){
  Serial.begin(9600);
  delay(1000);
  Serial.println();
  /*Serial.print("MAC: ");
  Serial.println(WiFi.macAddress());*/
  Serial.print("Setting soft-AP configuration ... ");
  Serial.println(WiFi.softAPConfig(local_IP, gateway, subnet) ? "Ready" : "Failed!");
  Serial.print("Setting soft-AP ... ");
  Serial.println(WiFi.softAP(ssid, password) ? "Ready" : "Failed!");
  delay(2000);
  Serial.print("Soft-AP IP address = ");
  Serial.println(WiFi.softAPIP());
  Serial.print("Soft-AP Mac adress address = ");
  Serial.println(WiFi.softAPmacAddress());
  Serial.print("Local IP address = ");
  Serial.println(WiFi.localIP());

  // Route for root / web page
  server.on("/", HTTP_GET, [](AsyncWebServerRequest *request){
    request->send(200, "text/html", index_html);
  });
  server.on("/send", HTTP_GET, [](AsyncWebServerRequest *request){
    handleForm(request);
    lcd_set_text(s);
  });

  // Start server
  server.begin();
  Serial.println("HTTP server started");

  lcd_init();
}
unsigned long previous_millis = 0;
const long interval_millis = 1000;

void loop() {
  unsigned long current_millis = millis();
  if (current_millis - previous_millis >= interval_millis) {
    seconds_elapsed += 1;
    Serial.println(seconds_elapsed);
    previous_millis = current_millis;
  }
}