# Config Assistant POC
This repository is regarding the config assistant which will do bulk commit  

## Code changes
To see the changes that have been done for this config assistant got to [Conf_Assist_Commit](https://github.com/Vibaswan/ixnetwork_restpy/commit/e52b04e6cd8a704ec14b53863802cea070c648ca)
## Key Features
* Config Assistant for bulk commit
* New way for configuring traffic (protocol template auto generated)
* Ability to save config as Json (part of bulk commit)

## Install the client
```
pip install wheel-name
```
The wheel can be found in the link [Wheel](wheel)

## Import the package
Import a package based on your product:
```python
# The ixnetwork_restpy package is the superset of all IxNetwork products
from ixnetwork_restpy import SessionAssistant
```


## Start scripting
The sample script can be found in the link [Sample_Script](Sample_Script)
```python
"""This script demonstrates how to get started with ixnetwork_restpy scripting.

The script demonstrates the following:
    - connect to an IxNetwork test platform, authenticate, add a new session and clear the config
    - create vport and toplogy
    - create traffic
    - assign ports
    - do some more changes
    - start protocol stack and traffic  
"""
from ixnetwork_restpy import SessionAssistant

session_assistant = SessionAssistant(IpAddress='127.0.0.1', UserName='admin', Password='admin',
                                     LogLevel=SessionAssistant.LOGLEVEL_INFO, ClearConfig=True)
ixnetwork = session_assistant.Ixnetwork

conf_assist = session_assistant.ConfigAssistant()
config = conf_assist.config
vport = config.Vport.add().add()
vport[0].Name = 'myVport_1'
vport[0].RxMode = 'captureAndMeasure'
vport[1].Name = 'myVport_2'
topo = config.Topology.add(Name='Topology 1', Vports=vport[0]).add(Name='Topology 2', Vports=vport[1])
for i in range(0, 2):
    eth1 = topo[0].DeviceGroup.add(Name='Device Group 1', Multiplier='4').Ethernet.add()
    eth1.Mac.Increment(start_value='00:11:22:33:44:55', step_value='00:11:01:00:00:01')
    eth1.Mtu.Single('1670')
    ipv41 = eth1.Ipv4.add(Name='Ipv4 East')
    ipv41.Address.Increment(start_value='1.1.1.1', step_value='0.1.0.0')
    ipv41.GatewayIp.Increment(start_value='1.1.1.0', step_value='0.1.0.0')
    ipv41.Prefix.Single('26')
    eth2 = topo[1].DeviceGroup.add(Name='Device Group 2', Multiplier='4').Ethernet.add()
    eth2.Mac.Increment(start_value='00:55:44:33:22:11', step_value='00:10:01:00:00:21')
    eth2.Mtu.Single('1770')
    ipv42 = eth2.Ipv4.add(Name='Ipv4 West')
    ipv42.Address.Increment(start_value='1.1.1.0', step_value='0.1.0.0')
    ipv42.GatewayIp.Increment(start_value='1.1.1.1', step_value='0.1.0.0')
    ipv42.Prefix.Single('26')
traffic = config.Traffic.TrafficItem
for i in range(0, 2):
    tr1 = traffic.add(Name='RAW TCP', BiDirectional=False, TrafficType='raw', TrafficItemType='l2L3')
    tr1.EndpointSet.add(Sources=vport[0].Protocols, Destinations=vport[1].Protocols)
    stack = tr1.ConfigElement.Stack
    eth_st = stack.Ethernet_II.add()
    eth_st.Source_MAC_Address.Single('00:11:00:00:22:00')
    eth_st.Destination_MAC_Address.Single('00:33:00:11:22:00')
    ipv4_st = stack.IPv4.add()
    ipv4_st[0].Source_Address.Increment(start_value='1.1.1.1', step_value='0.1.0.1')
    ipv4_st[0].Destination_Address.Increment(start_value='2.2.2.2', step_value='0.1.0.1')
    ipv4_st[0].TTL_Time_to_live.Single('56')
    ipv4_st[0].Identification.Single('1')
    tcp_st = stack.TCP.add()
    tcp_st.TCP_Source_Port.Single('80')
    tcp_st.TCP_Dest_Port.Single('70')
    tcp_st.Sequence_Number.Single('0x45')
    tcp_st.Acknowledgement_Number.Single('0xcc')
    udp_st = stack.UDP.add()
    udp_st.UDP_Dest_Port.Single('77')
    udp_st.UDP_Source_Port.Single('66')
    udp_st.UDP_Length.Single('12')
print(json.dumps(conf_assist.config_json, indent=4, sort_keys=True))
errs = conf_assist.commit()
if errs is not None:
    raise Exception('json import has errors %s' % str(errs))

chassis_ip = '10.36.74.205'
test_ports = [
    dict(Arg1=chassis_ip, Arg2=1, Arg3=13),
    dict(Arg1=chassis_ip, Arg2=1, Arg3=14)
]

connected_ports = config.AssignPorts(test_ports, [], vport, True)
eth1.Start()

print('changing something after commit')
vport[0].Name = 'changed_vport_1'
vport.add(Name='new_vport')
eth = config.Topology.add(Name='Topology_3', Vports=vport[-1])[-1].DeviceGroup.add(Multiplier=5, Name='dg1').\
    Ethernet.add()
eth.Mac.Increment(start_value='00:11:22:33:44:55', step_value='00:11:01:00:00:01')
eth.Mtu.Single('1670')
print(json.dumps(conf_assist.config_json, indent=4, sort_keys=True))
conf_assist.commit()
chassis_ip = '10.36.74.205'
test_ports = [
    dict(Arg1=chassis_ip, Arg2=1, Arg3=20),
]

config.AssignPorts(test_ports, [], vport[-1], True)
eth.Start()
config.Traffic.Apply()
config.Traffic.Start()
```

## Supported Server Versions
This client package supports versions 8.52 and up of the following servers:
* Linux IxNetwork API Server
* Windows IxNetwork GUI
* Windows IxNetwork Connection Manager


## Contributing
The purpose of this repository is to allow others see how much of a progress made and spread the findings of the poc to a broader audience for feedback .
