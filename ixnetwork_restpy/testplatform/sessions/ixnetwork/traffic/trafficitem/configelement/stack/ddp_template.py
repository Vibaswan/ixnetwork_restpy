from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class DDP(Base):
    __slots__ = ()
    _SDM_NAME = 'ddp'
    _SDM_ATT_MAP = {
        'DDP Packet header': 'ddp.header.header',
    }

    def __init__(self, parent):
        super(DDP, self).__init__(parent)

    @property
    def DDP_Packet_header(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DDP Packet header']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
