from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Link_OAM(Base):
    __slots__ = ()
    _SDM_NAME = 'linkOAM'
    _SDM_ATT_MAP = {
        'OAM Packet': 'linkOAM.header.packet',
        'Frame Check Sequence CRC-32': 'linkOAM.header.fcs',
    }

    def __init__(self, parent):
        super(Link_OAM, self).__init__(parent)

    @property
    def OAM_Packet(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['OAM Packet']))

    @property
    def Frame_Check_Sequence_CRC_32(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Frame Check Sequence CRC-32']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
