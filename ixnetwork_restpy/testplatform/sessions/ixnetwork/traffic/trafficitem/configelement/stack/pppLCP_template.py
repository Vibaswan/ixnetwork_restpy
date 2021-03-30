from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class PPP_LCP(Base):
    __slots__ = ()
    _SDM_NAME = 'pppLCP'
    _SDM_ATT_MAP = {
        'Code': 'pppLCP.header.opcode',
        'Identifier': 'pppLCP.header.identifier',
        'Length': 'pppLCP.header.length',
        'Data': 'pppLCP.header.data',
    }

    def __init__(self, parent):
        super(PPP_LCP, self).__init__(parent)

    @property
    def Code(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Code']))

    @property
    def Identifier(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Identifier']))

    @property
    def Length(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Length']))

    @property
    def Data(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Data']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
