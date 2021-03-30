from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class VXLAN(Base):
    __slots__ = ()
    _SDM_NAME = 'vxlan'
    _SDM_ATT_MAP = {
        'Flags': 'vxlan.header.flags',
        'Reserved': 'vxlan.header.reserved',
        'VNI': 'vxlan.header.vni',
        'Reserved8': 'vxlan.header.reserved8',
    }

    def __init__(self, parent):
        super(VXLAN, self).__init__(parent)

    @property
    def Flags(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Flags']))

    @property
    def Reserved(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Reserved']))

    @property
    def VNI(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['VNI']))

    @property
    def Reserved8(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Reserved8']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
