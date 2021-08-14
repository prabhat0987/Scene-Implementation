import paho.mqtt.client as mqttClient
import json


room1 = "bedroom"

broker_address = "127.0.0.1"
port = 1883

br = mqttClient.Client( room1 )

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


#callback for br client
def on_message_br( client, userdata, message ):
    scene = ( (message.payload).decode() )[2:]
    if scene == "stop":
        print( "BR: CC stopped" )
    else:
        #trigger devices in BR
        print( "BR: Received message from CC")
        try:
            scene_d = json.dumps(jdb[scene])
            br.publish( room1 + "/", scene_d )
            print( "BR: Implementing scene:" + scene )
        except KeyError:
            print("Scene not found")
        jfile.close()


br.on_connect = on_connect
br.on_message = on_message_br
br.connect( broker_address, port )

br.loop_start()

br.subscribe( "Control_Center/bedroom/" )
br.subscribe( "Control_Center/global/" )
br.subscribe( "Control_Center/stop/" )


try:
    while True:
        #time.sleep(1)
        pass

except KeyboardInterrupt:
    br.disconnect()
    br.loop_stop()