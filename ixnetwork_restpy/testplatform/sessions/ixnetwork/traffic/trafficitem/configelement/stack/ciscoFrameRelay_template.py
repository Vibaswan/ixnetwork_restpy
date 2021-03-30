from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Cisco_Frame_Relay(Base):
    __slots__ = ()
    _SDM_NAME = 'ciscoFrameRelay'
    _SDM_ATT_MAP = {
        'FrameRelayTag': 'ciscoFrameRelay.header.frameRelayTag',
        'Ethernet Type': 'ciscoFrameRelay.header.etherType',
    }

    def __init__(self, parent):
        super(Cisco_Frame_Relay, self).__init__(parent)

    @property
    def FrameRelayTag(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FrameRelayTag']))

    @property
    def Ethernet_Type(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Ethernet Type']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
