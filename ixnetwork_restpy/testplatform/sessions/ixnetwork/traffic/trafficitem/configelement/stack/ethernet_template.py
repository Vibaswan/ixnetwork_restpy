from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Ethernet_II(Base):
    __slots__ = ()
    _SDM_NAME = 'ethernet'
    _SDM_ATT_MAP = {
        'Destination MAC Address': 'ethernet.header.destinationAddress-1',
        'Source MAC Address': 'ethernet.header.sourceAddress-2',
        'Ethernet-Type': 'ethernet.header.etherType-3',
        'PFC Queue': 'ethernet.header.pfcQueue-4',
    }

    def __init__(self, parent):
        super(Ethernet_II, self).__init__(parent)

    @property
    def Destination_MAC_Address(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Destination MAC Address']))

    @property
    def Source_MAC_Address(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Source MAC Address']))

    @property
    def Ethernet_Type(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Ethernet-Type']))

    @property
    def PFC_Queue(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PFC Queue']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
