from time import time
import json
from ixnetwork_restpy import SessionAssistant

session_assistant = SessionAssistant(IpAddress='127.0.0.1', UserName='admin', Password='admin',
                                     LogLevel=SessionAssistant.LOGLEVEL_INFO, ClearConfig=True)
ixnetwork = session_assistant.Ixnetwork

conf_assist = session_assistant.ConfigAssistant()

start_time = time()
config = conf_assist.config
vport1 = config.Vport.add()[-1]
vport1.Name = 'myVport_1'
vport1.RxMode = 'captureAndMeasure'
vport2 = config.Vport.add()[-1]
vport2.Name = 'myVport_2'
config.Topology.add(Name='Topology 1', Vports=vport1).DeviceGroup.add(Name='Device Group 1', Multiplier='4').\
    Ethernet.add().Ipv4.add()
config.Topology.add(Name='Topology 2', Vports=vport2).DeviceGroup.add(Name='Device Group 1', Multiplier='4').\
    Ethernet.add().Ipv4.add()
for i in range(0, 10):
    config.Traffic.TrafficItem.add(Name='RAW TCP', BiDirectional=False, TrafficType='raw', TrafficItemType='l4l5').\
        EndpointSet.add(Sources=vport1.Protocols, Destinations=vport2.Protocols)
    config.Traffic.TrafficItem.ConfigElement.Stack.Ethernet_II.add()
print(json.dumps(conf_assist.config_json, indent=4, sort_keys=True))
conf_assist.commit()
end_time = time()
print(end_time - start_time)