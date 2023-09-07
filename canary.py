import json
import pyeapi



switches = ['leaf1', 'leaf2', 'leaf3', 'leaf4']

canary_MAC = "001c.73cd.693d"



for switch in switches:
    connect = pyeapi.connect_to(switch)
    output = connect.run_commands(['show bgp evpn route-type mac-ip'])
    print(output)
    if canary_MAC in output:
        print(switch, "has the canary")
