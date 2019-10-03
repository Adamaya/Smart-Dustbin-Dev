#include <ESP8266WiFi.h>
#include <PubSubClient.h>

#define trig_pin1 D6
#define echo_pin1 D5
const int trig_pin2=1;
const int echo_pin2=3;
int pulsevalue;
const char* ssid = "Eluga Ray Max";//"Eluga Ray Max LAPTOP-ADD3QHF2 5070"                   // wifi ssid
const char* password =  "adam3425";
const char* mqttServer = "192.168.43.218";
const int mqttPort = 1883;
const char* mqttUser = "dustbin2";      // if you don't have MQTT Username, no need input
const char* mqttPassword = "12345678";  // if you don't have MQTT Password, no need input
char msg1[50],msg2[50];
long duration1,duration2;
int aver1[3],aver2[3];
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


  Serial.begin(115200);// put your setup code here, to run once:
  pinMode(trig_pin1,OUTPUT);
  pinMode(echo_pin1,INPUT);
  pinMode(trig_pin2,OUTPUT);
  pinMode(echo_pin2,INPUT);
  delay(5);
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
    client.publish("container2DataGreen", msg1);            // change container name according to dustbin // publishing message
    client.subscribe("container2DataGreen");                 // subscribing data
    delay(1000);
    client.loop();
  }
  for(int i=0;i<3;i++){
  digitalWrite(trig_pin2, LOW);
  delayMicroseconds(5);
  digitalWrite(trig_pin2, HIGH);
  delayMicroseconds(15);
  digitalWrite(trig_pin2, LOW);
  pinMode(echo_pin2, INPUT);
  duration2 = pulseIn(echo_pin2, HIGH);
  int dist2 = (duration2*0.034)/2;                          //obtain distance
  aver1[i]=dist2; 
  delay(5);
  }
  int distance2=(aver2[0]+aver2[1]+aver2[2])/3;
  snprintf(msg2, 50, "%ld", distance2); 
  {
    client.publish("container2DataBlue", msg2);           // change container name according to dustbin
    client.subscribe("container2DataBlue");
    delay(1000);
    client.loop();
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
