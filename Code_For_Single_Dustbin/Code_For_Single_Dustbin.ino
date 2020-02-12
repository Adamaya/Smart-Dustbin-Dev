#include <ESP8266WiFi.h>
#include <PubSubClient.h>

#define trig_pin1 D7
#define echo_pin1 D8
int pulsevalue;
const char* ssid = "SDR";//"Eluga Ray Max LAPTOP-ADD3QHF2 5070"                   // wifi ssid
const char* password =  "rapidgadfly782";
const char* mqttServer = "192.168.31.74";
const int mqttPort = 1883;
const char* mqttUser = "dustbin2";      // if you don't have MQTT Username, no need input
const char* mqttPassword = "12345678";  // if you don't have MQTT Password, no need input
char msg1[50];                          //character array for message
long duration1;                         // long variable to store duration
int aver1[3];                           // integer array for holding 3 values of distance to find out its average
WiFiClient espClient;                   // declaring espClient as WiFiClient
PubSubClient client(espClient);         // declaring WiFiClient as pubsubclient

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);           //attempting wifi Connection

  while (WiFi.status() != WL_CONNECTED) {       
    delay(500);
    Serial.println("Connecting to WiFi..");
  }
  Serial.println("Connected to the WiFi network");

  //setting the MQTT Server and Port
  client.setServer(mqttServer, mqttPort);   
  client.setCallback(callback);

  //attempting Connection to MQTT Broker
  if (client.connect("ESP8266Client", mqttUser, mqttPassword )) { 
      delay(2000);
      Serial.println("connected");

    } else {

      Serial.print("failed with state ");
      Serial.print(client.state());
      delay(2000);}

  pinMode(trig_pin1,OUTPUT);
  pinMode(echo_pin1,INPUT);
}
void loop() {
  for (int i=0;i<=2;i++) {                                   // for average distance
  digitalWrite(trig_pin1, LOW);
  delayMicroseconds(5);
  digitalWrite(trig_pin1, HIGH);
  delayMicroseconds(15);
  digitalWrite(trig_pin1, LOW);
  pinMode(echo_pin1, INPUT);
  duration1 = pulseIn(echo_pin1, HIGH);
  int dist1 = (duration1*0.036)/2;                           //obtain distance
  aver1[i]=dist1; 
  delay(5);
  }
  int distance1=(aver1[0]+aver1[1]+aver1[2])/3;
  snprintf(msg1, 50, "%ld", distance1);                     // convert into char
  {
    client.publish("container2Data", msg1);            // change container name according to dustbin // publishing message
    client.subscribe("container2Data");                 // subscribing data
    delay(2000);

  }
}
void callback(char* topic, byte* payload, unsigned int length) {

  Serial.print("Message arrived in topic: ");
  Serial.println(topic);

  Serial.print("Message:");
  for (int i = 0; i < length; i++) {
    Serial.print((char)payload[i]);
  }
  Serial.println();
  Serial.println("-----------------------");
}
