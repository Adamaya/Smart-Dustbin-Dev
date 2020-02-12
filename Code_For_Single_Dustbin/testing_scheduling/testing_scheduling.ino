#include <ESP8266WiFi.h>
#include <PubSubClient.h>

const char* ssid = "Xiaomi_6A4F";//"Eluga Ray Max LAPTOP-ADD3QHF2 5070"                   // wifi ssid
const char* password =  "rapidgadfly781";
const char* mqttServer = "192.168.31.63";
const int mqttPort = 1883;
const char* mqttUser = "bin1";      // if you don't have MQTT Username, no need input
const char* mqttPassword = "12345678";
WiFiClient espClient;
PubSubClient client(espClient);

void setup() {
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.println("Connecting to WiFi..");
  }
  Serial.println("Connected to the WiFi network");

  client.setServer(mqttServer, mqttPort);
  client.setCallback(callback);

  if (client.connect("ESP8266Client", mqttUser, mqttPassword )) {
      delay(2000);
      Serial.println("connected");

    } else {

      Serial.print("failed with state ");
      Serial.print(client.state());
      delay(2000);}


  Serial.begin(9600);// put your setup code here, to run once:
  pinMode(D5,OUTPUT);
  delay(5);
  delay(150);
}

void loop(){
  client.subscribe("dustbinNo");
  client.loop();
  
}


void callback(char* topic, byte* payload, unsigned int length) {
  Serial.print("Message arrived [");
  Serial.print(topic);
  Serial.print("] ");
  for (int i = 0; i < length; i++) {
    Serial.print((char)payload[i]);
  }
  Serial.println();

  // Switch on the LED if an 1 was received as first character
  if ((char)payload[0] == '1') {
    digitalWrite(D5, LOW);   // Turn the LED on (Note that LOW is the voltage level
    // but actually the LED is on; this is because
    // it is active low on the ESP-01)
  } else {
    digitalWrite(D5, HIGH);  // Turn the LED off by making the voltage HIGH
  }

}
