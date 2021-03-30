from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class FCoE_NPIV_FDISC_LS_RJT(Base):
    __slots__ = ()
    _SDM_NAME = 'fCoENpivFdiscLsRjt'
    _SDM_ATT_MAP = {
        'FCoE Header': 'fCoENpivFdiscLsRjt.header.fcoeHeader',
        'FC Header': 'fCoENpivFdiscLsRjt.header.fcHeader',
        'FC ELS': 'fCoENpivFdiscLsRjt.header.FcEls',
    }

    def __init__(self, parent):
        super(FCoE_NPIV_FDISC_LS_RJT, self).__init__(parent)

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
