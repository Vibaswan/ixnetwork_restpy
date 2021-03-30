from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class BVLAN_Header(Base):
    __slots__ = ()
    _SDM_NAME = 'bVlanHeader'
    _SDM_ATT_MAP = {
        'Ethertype value': 'bVlanHeader.bTAGEthertype.ethertypeValue',
        'B-TAG': 'bVlanHeader.bTAGEthertype.bTag',
    }

    def __init__(self, parent):
        super(BVLAN_Header, self).__init__(parent)

    @property
    def Ethertype_value(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Ethertype value']))

    @property
    def B_TAG(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['B-TAG']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
