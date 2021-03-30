from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class AAL5(Base):
    __slots__ = ()
    _SDM_NAME = 'aal5'
    _SDM_ATT_MAP = {
        'AtmL2Header': 'aal5.atmL2Header.atmL2Header',
    }

    def __init__(self, parent):
        super(AAL5, self).__init__(parent)

    @property
    def AtmL2Header(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AtmL2Header']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
