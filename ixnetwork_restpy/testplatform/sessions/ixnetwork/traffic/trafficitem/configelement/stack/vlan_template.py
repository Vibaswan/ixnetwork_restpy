from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class VLAN(Base):
    __slots__ = ()
    _SDM_NAME = 'vlan'
    _SDM_ATT_MAP = {
        'VLAN-Tag': 'vlan.header.vlanTag',
        'Protocol-ID': 'vlan.header.protocolID',
    }

    def __init__(self, parent):
        super(VLAN, self).__init__(parent)

    @property
    def VLAN_Tag(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['VLAN-Tag']))

    @property
    def Protocol_ID(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Protocol-ID']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
