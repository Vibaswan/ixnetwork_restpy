from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class FIP_NPIV_FDISC_Request_ENode(Base):
    __slots__ = ()
    _SDM_NAME = 'fipNpivFdiscRequestEnode'
    _SDM_ATT_MAP = {
        'Version': 'fipNpivFdiscRequestEnode.header.fipVersion',
        'Reserved': 'fipNpivFdiscRequestEnode.header.fipReserved',
        'FIP Operation': 'fipNpivFdiscRequestEnode.header.fipOperation',
        'FIP Descriptors': 'fipNpivFdiscRequestEnode.header.fipDescriptors',
    }

    def __init__(self, parent):
        super(FIP_NPIV_FDISC_Request_ENode, self).__init__(parent)

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
