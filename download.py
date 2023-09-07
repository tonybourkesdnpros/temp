import json
import pyeapi
import os


directory = "configs"
exists = os.path.exists(directory)
if not exists:
    os.makedirs(directory)

switches = ['leaf1', 'leaf2', 'leaf3', 'leaf4', 'spine1', 'spine2', 'spine3']
for switch in switches:
    connect = pyeapi.connect_to(switch)
    output = connect.run_commands(['show running-config'], encoding='text')
    # print(output[0]['output'])    # 
    file = open(directory+'/'+switch+'.txt','w')
    print("Writing for", switch)
    file.write(output[0]['output'])
    file.close() 

