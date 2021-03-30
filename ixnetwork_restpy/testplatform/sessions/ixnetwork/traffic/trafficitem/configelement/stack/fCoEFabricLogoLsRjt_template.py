from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class FCoE_Fabric_LOGO_LS_RJT(Base):
    __slots__ = ()
    _SDM_NAME = 'fCoEFabricLogoLsRjt'
    _SDM_ATT_MAP = {
        'FCoE Header': 'fCoEFabricLogoLsRjt.header.fcoeHeader',
        'FC Header': 'fCoEFabricLogoLsRjt.header.fcHeader',
        'FC ELS': 'fCoEFabricLogoLsRjt.header.FcEls',
    }

    def __init__(self, parent):
        super(FCoE_Fabric_LOGO_LS_RJT, self).__init__(parent)

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
