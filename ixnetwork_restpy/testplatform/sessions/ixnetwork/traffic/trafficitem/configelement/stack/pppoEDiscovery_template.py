from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class PPPoE___Discovery(Base):
    __slots__ = ()
    _SDM_NAME = 'pppoEDiscovery'
    _SDM_ATT_MAP = {
        'PPPoE Header': 'pppoEDiscovery.header.header',
        'PPPoE Tags': 'pppoEDiscovery.header.tags',
    }

    def __init__(self, parent):
        super(PPPoE___Discovery, self).__init__(parent)

    @property
    def PPPoE_Header(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PPPoE Header']))

    @property
    def PPPoE_Tags(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PPPoE Tags']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
