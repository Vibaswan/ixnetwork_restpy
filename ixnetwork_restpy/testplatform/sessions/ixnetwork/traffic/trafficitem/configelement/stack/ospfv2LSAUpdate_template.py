from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class OSPFv2_LSA_Update_Packet(Base):
    __slots__ = ()
    _SDM_NAME = 'ospfv2LSAUpdate'
    _SDM_ATT_MAP = {
        'OSPFv2 Packet Header': 'ospfv2LSAUpdate.header.ospfv2PacketHeader',
        'Link-State Update Body': 'ospfv2LSAUpdate.header.linkStateUpdateBody',
    }

    def __init__(self, parent):
        super(OSPFv2_LSA_Update_Packet, self).__init__(parent)

    @property
    def OSPFv2_Packet_Header(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['OSPFv2 Packet Header']))

    @property
    def Link_State_Update_Body(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Link-State Update Body']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
