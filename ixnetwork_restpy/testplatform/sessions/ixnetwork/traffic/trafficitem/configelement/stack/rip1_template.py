from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class RIP1(Base):
    __slots__ = ()
    _SDM_NAME = 'rip1'
    _SDM_ATT_MAP = {
        'RIP1 Header': 'rip1.header.rip1Header',
        'Routing Table Entry': 'rip1.header.routingTableEntry',
    }

    def __init__(self, parent):
        super(RIP1, self).__init__(parent)

    @property
    def RIP1_Header(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RIP1 Header']))

    @property
    def Routing_Table_Entry(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Routing Table Entry']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
