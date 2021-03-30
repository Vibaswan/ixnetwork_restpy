from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class OSPFv3_Hello(Base):
    __slots__ = ()
    _SDM_NAME = 'ospfv3Hello'
    _SDM_ATT_MAP = {
        'OSPFv3 Packet Header': 'ospfv3Hello.header.ospfv3PacketHeader',
        'OSPFv3 Packet Body': 'ospfv3Hello.header.ospfv3PacketBody',
    }

    def __init__(self, parent):
        super(OSPFv3_Hello, self).__init__(parent)

    @property
    def OSPFv3_Packet_Header(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['OSPFv3 Packet Header']))

    @property
    def OSPFv3_Packet_Body(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['OSPFv3 Packet Body']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
