from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class RTMP(Base):
    __slots__ = ()
    _SDM_NAME = 'rtmp'
    _SDM_ATT_MAP = {
        'Message Type': 'rtmp .header.messageType',
    }

    def __init__(self, parent):
        super(RTMP, self).__init__(parent)

    @property
    def Message_Type(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Message Type']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
