from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class LLC_Bridged_Ethernet_8023(Base):
    __slots__ = ()
    _SDM_NAME = 'llcBridgedEthernet'
    _SDM_ATT_MAP = {
        'Logical Link Control(LLC) Header': 'llcBridgedEthernet.header.llcHeader',
        'Organizationally Unique Identifier (OUI)': 'llcBridgedEthernet.header.oui',
        'PID': 'llcBridgedEthernet.header.pid',
        'Padding': 'llcBridgedEthernet.header.pad',
    }

    def __init__(self, parent):
        super(LLC_Bridged_Ethernet_8023, self).__init__(parent)

    @property
    def Logical_Link_ControlLLC_Header(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Logical Link Control(LLC) Header']))

    @property
    def Organizationally_Unique_Identifier_OUI(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Organizationally Unique Identifier (OUI)']))

    @property
    def PID(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PID']))

    @property
    def Padding(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Padding']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
