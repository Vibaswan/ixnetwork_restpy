from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class LLC(Base):
    __slots__ = ()
    _SDM_NAME = 'llc'
    _SDM_ATT_MAP = {
        'DSAP': 'llc.header.dsap',
        'SSAP': 'llc.header.ssap',
        'Control field': 'llc.header.controlField',
    }

    def __init__(self, parent):
        super(LLC, self).__init__(parent)

    @property
    def DSAP(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DSAP']))

    @property
    def SSAP(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SSAP']))

    @property
    def Control_field(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Control field']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
