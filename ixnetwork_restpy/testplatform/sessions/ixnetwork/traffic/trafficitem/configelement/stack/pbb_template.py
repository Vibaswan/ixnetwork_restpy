from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class PBB_Header(Base):
    __slots__ = ()
    _SDM_NAME = 'pbb'
    _SDM_ATT_MAP = {
        'I-TAG': 'pbb.header.iTAG',
        'C-Ethernet Header': 'pbb.header.cEthernetHeader',
    }

    def __init__(self, parent):
        super(PBB_Header, self).__init__(parent)

    @property
    def I_TAG(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['I-TAG']))

    @property
    def C_Ethernet_Header(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['C-Ethernet Header']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
