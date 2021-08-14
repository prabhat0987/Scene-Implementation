import paho.mqtt.client as mqttClient
import json


dev1 = "l_led"
dev2 = "l_fan"
dev3 = "l_ac"
dev4 = "l_speaker"

l_led = mqttClient.Client(dev1)
l_fan = mqttClient.Client(dev2)
l_ac = mqttClient.Client(dev3)
l_speaker = mqttClient.Client(dev4)


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print( "DEV_l:Connected to broker" )
    else:
        print( "DEV_l:Connectioned failed" )


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

l_led.on_connect = on_connect
l_led.on_message = on_message_dev1
l_led.connect( broker_address, port )

l_fan.on_connect = on_connect
l_fan.on_message = on_message_dev2
l_fan.connect( broker_address, port )

l_ac.on_connect = on_connect
l_ac.on_message = on_message_dev3
l_ac.connect( broker_address, port )

l_speaker.on_connect = on_connect
l_speaker.on_message = on_message_dev4
l_speaker.connect( broker_address, port )

l_led.loop_start()
l_ac.loop_start()
l_fan.loop_start()
l_speaker.loop_start()

l_led.subscribe( "livroom/" )
l_fan.subscribe( "livroom/" )
l_ac.subscribe( "livroom/" )
l_speaker.subscribe( "livroom/" )


try:
    while True:
        #time.sleep(1)
        pass

except KeyboardInterrupt:
    l_led.disconnect()
    l_fan.disconnect()
    l_ac.disconnect()
    l_speaker.disconnect()
    l_led.loop_stop()
    l_fan.loop_stop()
    l_ac.loop_stop()
    l_speaker.loop_stop()