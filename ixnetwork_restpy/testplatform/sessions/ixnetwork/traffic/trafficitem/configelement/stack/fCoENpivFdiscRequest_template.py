from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class FCoE_NPIV_FDISC_Request(Base):
    __slots__ = ()
    _SDM_NAME = 'fCoENpivFdiscRequest'
    _SDM_ATT_MAP = {
        'FCoE Header': 'fCoENpivFdiscRequest.header.fcoeHeader',
        'FC Header': 'fCoENpivFdiscRequest.header.fcHeader',
        'FC ELS': 'fCoENpivFdiscRequest.header.FcEls',
    }

    def __init__(self, parent):
        super(FCoE_NPIV_FDISC_Request, self).__init__(parent)

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
