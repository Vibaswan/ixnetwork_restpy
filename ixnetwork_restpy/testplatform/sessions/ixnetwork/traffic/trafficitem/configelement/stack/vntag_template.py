from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class VNTAG(Base):
    __slots__ = ()
    _SDM_NAME = 'vntag'
    _SDM_ATT_MAP = {
        'VNTag': 'vntag.header.vntagHeader',
        'Protocol-ID': 'vntag.header.protocolID',
    }

    def __init__(self, parent):
        super(VNTAG, self).__init__(parent)

    @property
    def VNTag(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['VNTag']))

    @property
    def Protocol_ID(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Protocol-ID']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
