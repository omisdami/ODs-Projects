#include <Wire.h>
#include "MAX30105.h"
#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>

// Replace with your network credentials
const char *ssid = "............";
const char *password = "60@west1";

// Create an object of the MAX3010x sensor
MAX30105 particleSensor;

// Create an object of the ESP8266WebServer class
ESP8266WebServer server(80);

void setup() {
  // Start Serial communication
  Serial.begin(115200);

  // Connect to Wi-Fi
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(250);
    Serial.print(".");
  }
  Serial.println("..");
  Serial.println("WiFi connected");
  Serial.println("..");
  Serial.println("WiFi connected");

  // Initialize the MAX3010x sensor
  if (!particleSensor.begin(Wire, I2C_SPEED_FAST)) {
    Serial.println("MAX30105 sensor not found. Please check wiring/power.");
    while (1);
  }

  // Set up the MAX3010x sensor
  particleSensor.setup();

  // Define server routes
  server.on("/", HTTP_GET, handleRoot);

  // Start server
  server.begin();
  Serial.println("HTTP server started");
}

void loop() {
  // Handle client requests
  server.handleClient();

  // Other code or delay can be added here
  delay(1000);
}

// Function to handle the root URL
void handleRoot() {
  String page = "<html><body>";
  page += "<h1>MAX30105 Sensor Data</h1>";
  
  // Read data from the sensor
  if (particleSensor.available()) {
    // Read the red and IR values
    uint32_t irValue = particleSensor.getIR();
    uint32_t redValue = particleSensor.getRed();

    // Display the values on the webpage
    page += "<p>IR Value: " + String(irValue) + "</p>";
    page += "<p>Red Value: " + String(redValue) + "</p>";
  } else {
    page += "<p>No data available from MAX30105 sensor.</p>";
  }

  page += "</body></html>";

  // Send the HTML page to the client
  server.send(200, "text/html", page);
}

