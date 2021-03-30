from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class OSPFv2_LSA_ACK_Packet(Base):
    __slots__ = ()
    _SDM_NAME = 'ospfv2LSAAcknowledgement'
    _SDM_ATT_MAP = {
        'OSPFv2 Packet Header': 'ospfv2LSAAcknowledgement.header.ospfv2PacketHeader',
        'Link-State Advertisement Header': 'ospfv2LSAAcknowledgement.header.linkStateAdvertisementHeader',
    }

    def __init__(self, parent):
        super(OSPFv2_LSA_ACK_Packet, self).__init__(parent)

    @property
    def OSPFv2_Packet_Header(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['OSPFv2 Packet Header']))

    @property
    def Link_State_Advertisement_Header(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Link-State Advertisement Header']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
