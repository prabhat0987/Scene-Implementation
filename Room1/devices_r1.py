import paho.mqtt.client as mqttClient
import json


dev1 = "b_led"
dev2 = "b_fan"
dev3 = "b_ac"
dev4 = "b_speaker"

b_led = mqttClient.Client( dev1 )
b_fan = mqttClient.Client( dev2 )
b_ac = mqttClient.Client( dev3 )
b_speaker = mqttClient.Client( dev4 )


#callback on connect
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print( "DEV_b:Connected to broker" )
    else:
        print( "DEV_b:Connection failed" )


def on_message_dev1(client, userdata, message):
    scene = json.loads( (message.payload).decode() )
    led_bright = scene["led_brightness"]
    led_color = scene["led_color"]
    print("LED:Implemented")


def on_message_dev2(client, userdata, message):
    scene = json.loads( (message.payload).decode() )
    speed = scene["fan"]
    print("FAN:Implemented")


def on_message_dev3(client, userdata, message):
    scene = json.loads( (message.payload).decode() )
    temp = scene["ac"]
    print("AC:Implemented")


def on_message_dev4(client, userdata, message):
    scene = json.loads( (message.payload).decode() )
    sound = scene["speaker"]
    print("SPEAKER:Implemented")


broker_address = "127.0.0.1"
port = 1883

b_led.on_connect = on_connect
b_led.on_message = on_message_dev1
b_led.connect( broker_address, port )

b_fan.on_connect = on_connect
b_fan.on_message = on_message_dev2
b_fan.connect( broker_address, port )

b_ac.on_connect = on_connect
b_ac.on_message = on_message_dev3
b_ac.connect( broker_address, port )

b_speaker.on_connect = on_connect
b_speaker.on_message = on_message_dev4
b_speaker.connect( broker_address, port )

b_led.loop_start()
b_ac.loop_start()
b_fan.loop_start()
b_speaker.loop_start()

b_led.subscribe( "bedroom/" )
b_fan.subscribe( "bedroom/" )
b_ac.subscribe( "bedroom/" )
b_speaker.subscribe( "bedroom/" )


try:
    while True:
        #time.sleep(1)
        pass

except KeyboardInterrupt:
    b_led.disconnect()
    b_fan.disconnect()
    b_ac.disconnect()
    b_speaker.disconnect()
    b_led.loop_stop()
    b_fan.loop_stop()
    b_ac.loop_stop()
    b_speaker.loop_stop()