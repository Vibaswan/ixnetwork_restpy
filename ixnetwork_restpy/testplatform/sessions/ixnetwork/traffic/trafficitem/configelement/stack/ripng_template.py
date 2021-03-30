from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class RIPng(Base):
    __slots__ = ()
    _SDM_NAME = 'ripng'
    _SDM_ATT_MAP = {
        'RIPng Header': 'ripng.header.ripngHeader',
        'Route Table entries': 'ripng.header.routeTableEntries',
    }

    def __init__(self, parent):
        super(RIPng, self).__init__(parent)

    @property
    def RIPng_Header(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RIPng Header']))

    @property
    def Route_Table_entries(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Route Table entries']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
