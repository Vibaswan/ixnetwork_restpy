from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class OAM_Depricated(Base):
    __slots__ = ()
    _SDM_NAME = 'oamCCM'
    _SDM_ATT_MAP = {
        'OAM Packet Type': 'oamCCM.header.oamPacketType',
    }

    def __init__(self, parent):
        super(OAM_Depricated, self).__init__(parent)

    @property
    def OAM_Packet_Type(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['OAM Packet Type']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
