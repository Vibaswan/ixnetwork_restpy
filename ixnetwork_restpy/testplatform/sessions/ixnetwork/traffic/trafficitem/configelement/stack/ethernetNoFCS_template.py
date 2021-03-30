from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Ethernet_II_without_FCS(Base):
    __slots__ = ()
    _SDM_NAME = 'ethernetNoFCS'
    _SDM_ATT_MAP = {
        'Destination MAC Address': 'ethernetNoFCS.header.destinationAddress',
        'Source MAC Address': 'ethernetNoFCS.header.sourceAddress',
        'Ethernet-Type': 'ethernetNoFCS.header.etherType',
    }

    def __init__(self, parent):
        super(Ethernet_II_without_FCS, self).__init__(parent)

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

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
