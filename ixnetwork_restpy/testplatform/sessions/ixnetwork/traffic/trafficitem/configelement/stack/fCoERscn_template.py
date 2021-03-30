from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class FCoE_RSCN(Base):
    __slots__ = ()
    _SDM_NAME = 'fCoERscn'
    _SDM_ATT_MAP = {
        'FCoE Header': 'fCoERscn.header.fcoeHeader',
        'FC Header': 'fCoERscn.header.fcHeader',
        'FC ELS': 'fCoERscn.header.FcEls',
    }

    def __init__(self, parent):
        super(FCoE_RSCN, self).__init__(parent)

    @property
    def FCoE_Header(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FCoE Header']))

    @property
    def FC_Header(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FC Header']))

    @property
    def FC_ELS(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FC ELS']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
