from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class VCMux_PPP(Base):
    __slots__ = ()
    _SDM_NAME = 'vcMuxPPP'
    _SDM_ATT_MAP = {
        'PPP Protocol Type': 'vcMuxPPP.header.pppProtocolType',
    }

    def __init__(self, parent):
        super(VCMux_PPP, self).__init__(parent)

    @property
    def PPP_Protocol_Type(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PPP Protocol Type']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
