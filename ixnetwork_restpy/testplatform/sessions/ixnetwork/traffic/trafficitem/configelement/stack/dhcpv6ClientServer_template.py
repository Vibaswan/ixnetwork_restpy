from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class DHCPv6_Client_Server_Message(Base):
    __slots__ = ()
    _SDM_NAME = 'dhcpv6ClientServer'
    _SDM_ATT_MAP = {
        'Message Type': 'dhcpv6ClientServer.header.messageType',
        'Transaction ID': 'dhcpv6ClientServer.header.transactionId',
        'Next Option': 'dhcpv6ClientServer.header.nextOption',
    }

    def __init__(self, parent):
        super(DHCPv6_Client_Server_Message, self).__init__(parent)

    @property
    def Message_Type(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Message Type']))

    @property
    def Transaction_ID(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Transaction ID']))

    @property
    def Next_Option(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Next Option']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
