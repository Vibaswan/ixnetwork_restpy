from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class FabricPath(Base):
    __slots__ = ()
    _SDM_NAME = 'fabricpath'
    _SDM_ATT_MAP = {
        'Outer Destination MAC Address': 'fabricpath.fabricpathHeader.outerdestinationAddress',
        'Outer Source MAC Address': 'fabricpath.fabricpathHeader.outersrcAddress',
        'FP TAG': 'fabricpath.fabricpathHeader.fptag',
    }

    def __init__(self, parent):
        super(FabricPath, self).__init__(parent)

    @property
    def Outer_Destination_MAC_Address(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Outer Destination MAC Address']))

    @property
    def Outer_Source_MAC_Address(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Outer Source MAC Address']))

    @property
    def FP_TAG(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FP TAG']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
