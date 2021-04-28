import json
from time import  time
from src.ixnetwork_restpy.assistants.sessions.sessionassistant import SessionAssistant

session_assistant = SessionAssistant(IpAddress='127.0.0.1', UserName='admin', Password='admin',
                                     LogLevel=SessionAssistant.LOGLEVEL_INFO, ClearConfig=True)
ixnetwork = session_assistant.Ixnetwork

start_time1 = time()
conf_assist = session_assistant.ConfigAssistant()
config = conf_assist.config
for i in range(0, 20):
    vport = config.Vport.add()
    for j in range(0, 400):
        int1 = vport.Interface.add(Enabled=True)
        int1.Ipv4.add(Ip='1.1.1.1', Gateway='1.1.1.2')
        bgp = vport.Protocols.Bgp
        bgp.Enabled = True
        neighbor_range1 = bgp.NeighborRange.add(Interfaces=int1, Enabled=True, EnableBgpId=True)
        # int2 = vport[1].Interface.add(Enabled=True)
        # int2.Ipv4.add(Ip='1.1.1.2', Gateway='1.1.1.1')
        # bgp = vport[1].Protocols.find().Bgp
        # bgp.Enabled = True
        # neighbor_range2 = bgp.NeighborRange.add(Interfaces=int2, Enabled=True, EnableBgpId=True)

conf_assist.commit()
conf_time = str(time() - start_time1)


start_time2 = time()
for i in ixnetwork.Vport:
    for bgp_peer in i.Protocols.Bgp.NeighborRange:
        bgp_peer.Enabled = False

conf_assist.commit()
print('for configuring == ' + conf_time)
print('for updating ==' + str(time() - start_time2))

