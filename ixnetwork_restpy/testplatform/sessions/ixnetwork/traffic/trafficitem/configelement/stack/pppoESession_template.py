from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class PPPoE___Session(Base):
    __slots__ = ()
    _SDM_NAME = 'pppoESession'
    _SDM_ATT_MAP = {
        'PPP Header': 'pppoESession.header.header',
        'PPP Protocol-ID': 'pppoESession.header.protocolID',
    }

    def __init__(self, parent):
        super(PPPoE___Session, self).__init__(parent)

    @property
    def PPP_Header(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PPP Header']))

    @property
    def PPP_Protocol_ID(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PPP Protocol-ID']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
