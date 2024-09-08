import paho.mqtt.client as mqtt
import os

mqtt_topic = "test/topic"

if os.isatty(0):
    print("stdin is a TTY", flush=True)
else:
    print("stdin is not a TTY", flush=True)
if os.isatty(1):
    print("stdout is a TTY", flush=True)
else:
    print("stdout is not a TTY", flush=True)
if os.isatty(2):
    print("stderr is a TTY", flush=True)
else:
    print("stderr is not a TTY", flush=True)

print("Debug")
# print("Debug", flush=True)

def on_connect(client, userdata, flags, reason_code, properties):
    print(f"Connected with result code {reason_code}")
    # print(f"Connected with result code {reason_code}", flush=True)
    client.subscribe(mqtt_topic)

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    # print(msg.topic+" "+str(msg.payload), flush=True)

def on_log(mqttc, obj, level, string):
    print(string)    
    # print(string, flush=True)    

def on_subscribe(mqttc, obj, mid, reason_code_list, properties):
    print("Subscribed: "+str(mid)+" "+str(reason_code_list))
    # print("Subscribed: "+str(mid)+" "+str(reason_code_list), flush=True)

mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqttc.on_connect = on_connect
mqttc.on_message = on_message
mqttc.on_log = on_log
mqttc.on_subscribe = on_subscribe

mqttc.connect("broker", 1883, 60)

mqttc.loop_forever()
