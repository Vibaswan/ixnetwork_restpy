from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class RGMP(Base):
    __slots__ = ()
    _SDM_NAME = 'rgmp'
    _SDM_ATT_MAP = {
        'Type': 'rgmp.header.type',
        'Reserved': 'rgmp.header.reserved',
        'Checksum': 'rgmp.header.checksum',
        'Multicast address': 'rgmp.header.multicastAddress',
    }

    def __init__(self, parent):
        super(RGMP, self).__init__(parent)

    @property
    def Type(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Type']))

    @property
    def Reserved(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Reserved']))

    @property
    def Checksum(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Checksum']))

    @property
    def Multicast_address(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Multicast address']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
