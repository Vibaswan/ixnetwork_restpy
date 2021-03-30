from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class FC_FLOGI_LS_RJT(Base):
    __slots__ = ()
    _SDM_NAME = 'fcFlogiLsRjt'
    _SDM_ATT_MAP = {
        'FC Header': 'fcFlogiLsRjt.header.fcHeader',
        'FC ELS': 'fcFlogiLsRjt.header.FcEls',
    }

    def __init__(self, parent):
        super(FC_FLOGI_LS_RJT, self).__init__(parent)

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
