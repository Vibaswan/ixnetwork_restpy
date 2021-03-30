from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class OSPFv2_LSA_Request_Packet(Base):
    __slots__ = ()
    _SDM_NAME = 'ospfv2LSARequest'
    _SDM_ATT_MAP = {
        'OSPFv2 Packet Header': 'ospfv2LSARequest.header.ospfv2PacketHeader',
        'Link-State Request Body': 'ospfv2LSARequest.header.linkStateRequestBody',
    }

    def __init__(self, parent):
        super(OSPFv2_LSA_Request_Packet, self).__init__(parent)

    @property
    def OSPFv2_Packet_Header(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['OSPFv2 Packet Header']))

    @property
    def Link_State_Request_Body(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Link-State Request Body']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
