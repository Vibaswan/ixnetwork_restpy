from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Virtual_Circuit_Multiplexed_Bridged_Ethernet_8023(Base):
    __slots__ = ()
    _SDM_NAME = 'vcMuxBridgedEthernet'
    _SDM_ATT_MAP = {
        'Padding': 'vcMuxBridgedEthernet.header.pad',
    }

    def __init__(self, parent):
        super(Virtual_Circuit_Multiplexed_Bridged_Ethernet_8023, self).__init__(parent)

    @property
    def Padding(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Padding']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
