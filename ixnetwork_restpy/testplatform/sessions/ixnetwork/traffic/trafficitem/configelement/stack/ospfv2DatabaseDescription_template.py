from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class OSPFv2_Database_Description_Packet(Base):
    __slots__ = ()
    _SDM_NAME = 'ospfv2DatabaseDescription'
    _SDM_ATT_MAP = {
        'OSPFv2 Packet Header': 'ospfv2DatabaseDescription.header.ospfv2PacketHeader',
        'Database Description Body': 'ospfv2DatabaseDescription.header.databaseDescriptionBody',
    }

    def __init__(self, parent):
        super(OSPFv2_Database_Description_Packet, self).__init__(parent)

    @property
    def OSPFv2_Packet_Header(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['OSPFv2 Packet Header']))

    @property
    def Database_Description_Body(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Database Description Body']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
