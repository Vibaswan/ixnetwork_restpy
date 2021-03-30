from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class IPv6_Pseudo_Header(Base):
    __slots__ = ()
    _SDM_NAME = 'ipv6Pseudo'
    _SDM_ATT_MAP = {
        'Source Address': 'ipv6Pseudo.header.srcAddress',
        'Destination Address': 'ipv6Pseudo.header.dstAddress',
        'Upper-Layer Packet Length': 'ipv6Pseudo.header.upperLayerPacketLength',
        'Zero': 'ipv6Pseudo.header.zero',
        'Next Header': 'ipv6Pseudo.header.nextHeader',
    }

    def __init__(self, parent):
        super(IPv6_Pseudo_Header, self).__init__(parent)

    @property
    def Source_Address(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Source Address']))

    @property
    def Destination_Address(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Destination Address']))

    @property
    def Upper_Layer_Packet_Length(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Upper-Layer Packet Length']))

    @property
    def Zero(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Zero']))

    @property
    def Next_Header(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Next Header']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
