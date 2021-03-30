from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class L2VPN_FR(Base):
    __slots__ = ()
    _SDM_NAME = 'l2VPNFrameRelay'
    _SDM_ATT_MAP = {
        'FR IP CW': 'l2VPNFrameRelay.header.controlWord',
    }

    def __init__(self, parent):
        super(L2VPN_FR, self).__init__(parent)

    @property
    def FR_IP_CW(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FR IP CW']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
