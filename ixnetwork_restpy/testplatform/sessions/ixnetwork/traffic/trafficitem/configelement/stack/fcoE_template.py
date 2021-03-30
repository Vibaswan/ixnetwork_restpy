from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class FCoE(Base):
    __slots__ = ()
    _SDM_NAME = 'fcoE'
    _SDM_ATT_MAP = {
        'FCoE Header': 'fcoE.header.fcoeHeader',
        'FC Header': 'fcoE.header.fcHeader',
    }

    def __init__(self, parent):
        super(FCoE, self).__init__(parent)

    @property
    def FCoE_Header(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FCoE Header']))

    @property
    def FC_Header(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FC Header']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
