from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class OSPFv3_LSA_Request_Packet(Base):
    __slots__ = ()
    _SDM_NAME = 'ospfv3LSARequest'
    _SDM_ATT_MAP = {
        'OSPFv3 Packet Header': 'ospfv3LSARequest.header.ospfv3PacketHeader',
        'Link-State Request Body': 'ospfv3LSARequest.header.linkStateRequestBody',
    }

    def __init__(self, parent):
        super(OSPFv3_LSA_Request_Packet, self).__init__(parent)

    @property
    def OSPFv3_Packet_Header(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['OSPFv3 Packet Header']))

    @property
    def Link_State_Request_Body(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Link-State Request Body']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
