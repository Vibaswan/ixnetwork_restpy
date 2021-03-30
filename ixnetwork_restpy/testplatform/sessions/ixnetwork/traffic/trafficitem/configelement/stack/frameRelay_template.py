from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Frame_Relay(Base):
    __slots__ = ()
    _SDM_NAME = 'frameRelay'
    _SDM_ATT_MAP = {
        'FrameRelayTag': 'frameRelay.header.frameRelayTag',
        'Control': 'frameRelay.header.control',
        'Padding': 'frameRelay.header.padding',
        'NLPID': 'frameRelay.header.nlpid',
    }

    def __init__(self, parent):
        super(Frame_Relay, self).__init__(parent)

    @property
    def FrameRelayTag(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FrameRelayTag']))

    @property
    def Control(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Control']))

    @property
    def Padding(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Padding']))

    @property
    def NLPID(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['NLPID']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
