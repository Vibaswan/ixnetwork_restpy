from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class RIP2(Base):
    __slots__ = ()
    _SDM_NAME = 'rip2'
    _SDM_ATT_MAP = {
        'RIP2 Header': 'rip2.header.rip2Header',
        'Authentication entry': 'rip2.header.authenticationEntry',
        'Routing Table Entry': 'rip2.header.routingTableEntry',
    }

    def __init__(self, parent):
        super(RIP2, self).__init__(parent)

    @property
    def RIP2_Header(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RIP2 Header']))

    @property
    def Authentication_entry(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Authentication entry']))

    @property
    def Routing_Table_Entry(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Routing Table Entry']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
