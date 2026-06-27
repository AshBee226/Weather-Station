#include <HTTPClient.h>
#include <WiFi.h>
#include <ArduinoJson.h>
#include <OneWire.h>
#include <DallasTemperature.h>

const int temperatureWire = 4;

OneWire oneWire(temperatureWire);
DallasTemperature sensors(&oneWire);

DynamicJsonDocument doc(2048);

<<<<<<< HEAD
=======


>>>>>>> ff3ae95ddbfcfcec3c6f4b989cfc20d49d052043
const char* serverName = "http://192.168.1.94:8000/sent";

unsigned long lastTime = 0;

unsigned long timerDelay = 5000; //change to 60000 for 1 minute

void setup() {
  Serial.begin(9600);

  sensors.begin();

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
}

void loop() {

  if ((millis() - lastTime) > timerDelay) {
    sensors.requestTemperatures();

    float message = sensors.getTempCByIndex(0);

    doc["message"] = message;
    delay(1000);
    
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
