#include <HTTPClient.h>
#include <WiFi.h>
#include <ArduinoJson.h>
#include <OneWire.h>
#include <DallasTemperature.h>

DynamicJsonDocument doc(2048);


const char* ssid = "ZTE_2.4G_PCJnGt";
const char* password = "7jU3c4zK";

const char* serverName = "http://192.168.1.94:8000/sent";

unsigned long lastTime = 0;

unsigned long timerDelay = 5000; //change to 60000 for 1 minute

void setup() {
  Serial.begin(9600);

  WiFi.begin(ssid, password);
  Serial.println("Connecting");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.print("Connected to WiFi network with local IP: ");
  Serial.println(WiFi.localIP());

  Serial.println("Timer set to 5 seconds");
}-

void loop() {

  while(Serial.available() == 0) {
  }

  String message = Serial.readString();
  message.replace("\n", "");

  doc["message"] = message;

  if ((millis() - lastTime) > timerDelay) {
    Serial.println("5s");
    if (WiFi.status() == WL_CONNECTED) {
      WiFiClient client;
      HTTPClient http;

      http.begin(client, serverName);

      http.addHeader("Content-Type", "application/json");

      String json;
      serializeJson(doc, json);

      int httpResponseCode = http.POST(json);


      Serial.print("HTTP Response code: ");
      Serial.println(httpResponseCode);

      http.end();
      lastTime = millis();
    }
    else
    Serial.println("WiFi Disconnected");
  }
}