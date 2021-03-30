from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class FIP_VLAN_Request(Base):
    __slots__ = ()
    _SDM_NAME = 'fipVlanRequest'
    _SDM_ATT_MAP = {
        'Version': 'fipVlanRequest.header.fipVersion',
        'Reserved': 'fipVlanRequest.header.fipReserved',
        'FIP Operation': 'fipVlanRequest.header.fipOperation',
        'FIP Descriptors': 'fipVlanRequest.header.fipDescriptors',
    }

    def __init__(self, parent):
        super(FIP_VLAN_Request, self).__init__(parent)

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
