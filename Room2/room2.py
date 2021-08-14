import paho.mqtt.client as mqttClient
import json


room2 = "livroom"

broker_address = "127.0.0.1"
port = 1883

lr = mqttClient.Client( room2 )

#opening scenes.json file
try:
    jfile = open( 'scenes.json', 'r+' )
    jdb = json.load( jfile )
    jfile.seek(0)
except FileNotFoundError:
    print( "File Not Found: scenes.json" )


#callback on connect
def on_connect( client, userdata, flags, rc ):
    if rc == 0 :
        print("Connected with result code:" + str(rc) )
    else:
        print("Connection failed with result code:" + str(rc))


#callback for lr client
def on_message_lr( client, userdata, message ):
    scene = ( (message.payload).decode() )[2:]
    if scene == "stop":
        print( "LR: CC stopped" )
    else:
        #trigger devices in BR
        print( "LR: Received message from CC" )
        try:
            scene_d = json.dumps(jdb[scene])
            lr.publish( room2 + "/", scene_d )
            print( "LR: Implementing scene:" + scene )
        except KeyError:
            print("Scene not found")
        jfile.close()


lr.on_connect = on_connect
lr.on_message = on_message_lr
lr.connect( broker_address, port )

lr.loop_start()

lr.subscribe( "Control_Center/living/" )
lr.subscribe( "Control_Center/global/" )
lr.subscribe( "Control_Center/stop/" )


try:
    while True:
        #time.sleep(1)
        pass

except KeyboardInterrupt:

    lr.disconnect
    lr.loop_stop()