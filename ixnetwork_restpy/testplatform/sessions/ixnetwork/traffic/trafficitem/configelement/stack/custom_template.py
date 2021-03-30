from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Custom(Base):
    __slots__ = ()
    _SDM_NAME = 'custom'
    _SDM_ATT_MAP = {
        'Length': 'custom.header.length',
        'Data': 'custom.header.data',
    }

    def __init__(self, parent):
        super(Custom, self).__init__(parent)

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
