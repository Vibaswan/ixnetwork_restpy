from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class DHCPv6_Relay_Agent_Server_Message(Base):
    __slots__ = ()
    _SDM_NAME = 'dhcpv6Relay'
    _SDM_ATT_MAP = {
        'Message Type': 'dhcpv6Relay.header.messageType',
        'Hop Count': 'dhcpv6Relay.header.hopCount',
        'Link Address': 'dhcpv6Relay.header.linkAddress',
        'Peer Address': 'dhcpv6Relay.header.peerAddress',
        'Next Option': 'dhcpv6Relay.header.nextOption',
    }

    def __init__(self, parent):
        super(DHCPv6_Relay_Agent_Server_Message, self).__init__(parent)

    @property
    def Message_Type(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Message Type']))

    @property
    def Hop_Count(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Hop Count']))

    @property
    def Link_Address(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Link Address']))

    @property
    def Peer_Address(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Peer Address']))

    @property
    def Next_Option(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Next Option']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
