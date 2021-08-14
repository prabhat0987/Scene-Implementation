import paho.mqtt.client as mqttClient
import time


#callback method
def on_connect(client, userdata, flags, rc) :

    if rc==0 :
        print("Connected with result code:" + str(rc) )
    else:
        print("Connection failed with result code:" + str(rc))


'''
def on_message( client, userdata, message) :
    print("Received message:" + str(message.payload) + "\non topic:" + message.topic + "\nwith QoS:" + str(message.qos) )
'''

client_name = "Control_Center"
broker_address = "127.0.0.1"       #broker address
port = 1883     #Broker port

control_c = mqttClient.Client( client_name )       #instance of mqttClient.client
control_c.on_connect = on_connect      #callback when connected
control_c.connect( broker_address, port )

control_c.loop_start()


#getting scene to implement
new_scene = input()
current_scene = ""
#if scene :
#    scene = "s_l_off"       #default scene is sunrise

#print( scene )

try:
    while True:
        if new_scene != current_scene :     #check for new input from user
            if new_scene[0] == 'b':
                control_c.publish( client_name + "/bedroom/", new_scene)
            elif new_scene[0] == 'l':
                control_c.publish( client_name + "/living/", new_scene)
            elif new_scene[0] == 'g':
                control_c.publish( client_name + "/global/", new_scene)

            current_scene = new_scene
        
        new_scene = input()


except KeyboardInterrupt:
    print("Stoping")
    control_c.publish( client_name + "/stop/", "stop")
    control_c.disconnect()
    control_c.loop_stop()