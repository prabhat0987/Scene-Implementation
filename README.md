### Scene-Implementation

This projects is in field of IoT and implements various scenes used by users at home.  
This projects uses mqtt service and hivemq as broker.  

MQTT can be installed using-  
For python2 - pip install paho-mqtt  
For python3 - pip3 install paho-mqtt  

Files and folders-

control_center.py - gets input scenes from user and publishes the scenes.  
Room2 - This folder contains devices and room control file corresponding to its own room.  
	room2.py, scenes.json, devices_r2.py, dev_conf  
Room1 - This folder contains devices and room control file corresponding to its own room.  
	room1.py, scenes.json, devices_r1.py, dev_conf  

Types of scenes-   
Room specific - scenes to be implemented in a particular scenes  
Global scenes - scenes to be implemented in all rooms  


Working of project  

1. User give a scene to implement to control_center(with "lr" or "br" concatinated at starting of each scene to distinguish the rooms).  
2. Control_center publishes this scene to a particular room or globally(to all rooms) depending on where to implement the scene.  
3. Room gets the scene from control_center.  
4. Room gets the device specifications of the scene from scenes.json file.  
5. Room publishes the device specifications.  
6. Each device belonging to the room gets its own specification regarding the scene.  
7. Each device executes its specification.  
