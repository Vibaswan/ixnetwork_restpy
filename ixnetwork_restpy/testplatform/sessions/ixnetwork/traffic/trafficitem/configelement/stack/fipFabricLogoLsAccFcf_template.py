from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class FIP_Fabric_LOGO_LS_ACC_FCF(Base):
    __slots__ = ()
    _SDM_NAME = 'fipFabricLogoLsAccFcf'
    _SDM_ATT_MAP = {
        'Version': 'fipFabricLogoLsAccFcf.header.fipVersion',
        'Reserved': 'fipFabricLogoLsAccFcf.header.fipReserved',
        'FIP Operation': 'fipFabricLogoLsAccFcf.header.fipOperation',
        'FIP Descriptors': 'fipFabricLogoLsAccFcf.header.fipDescriptors',
    }

    def __init__(self, parent):
        super(FIP_Fabric_LOGO_LS_ACC_FCF, self).__init__(parent)

    @property
    def Version(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Version']))

    @property
    def Reserved(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Reserved']))

    @property
    def FIP_Operation(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FIP Operation']))

    @property
    def FIP_Descriptors(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FIP Descriptors']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
