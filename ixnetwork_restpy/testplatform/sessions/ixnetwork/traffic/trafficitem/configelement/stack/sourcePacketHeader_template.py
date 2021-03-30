from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class IEC_61883_4_Source_Packet(Base):
    __slots__ = ()
    _SDM_NAME = 'sourcePacketHeader'
    _SDM_ATT_MAP = {
        'Reserved': 'sourcePacketHeader.header.reserved',
        'Cycle Count': 'sourcePacketHeader.header.cycleCount',
        'Cycle Offset': 'sourcePacketHeader.header.cycleOffset',
        'Transport Stream Packet': 'sourcePacketHeader.header.tSP',
    }

    def __init__(self, parent):
        super(IEC_61883_4_Source_Packet, self).__init__(parent)

    @property
    def Reserved(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Reserved']))

    @property
    def Cycle_Count(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Cycle Count']))

    @property
    def Cycle_Offset(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Cycle Offset']))

    @property
    def Transport_Stream_Packet(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Transport Stream Packet']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
