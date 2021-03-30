from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class INT_Shim_Header(Base):
    __slots__ = ()
    _SDM_NAME = 'intshimheader'
    _SDM_ATT_MAP = {
        'Type': 'intshimheader.shimheader.type',
        'Reserved': 'intshimheader.shimheader.reserved8',
        'Length (x4 bytes)': 'intshimheader.shimheader.length',
        'DSCP': 'intshimheader.shimheader.dscp',
        'Reserved': 'intshimheader.shimheader.reserved2',
    }

    def __init__(self, parent):
        super(INT_Shim_Header, self).__init__(parent)

    @property
    def Type(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Type']))

    @property
    def Reserved(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Reserved']))

    @property
    def Length_x4_bytes(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Length (x4 bytes)']))

    @property
    def DSCP(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DSCP']))

    @property
    def Reserved(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Reserved']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
