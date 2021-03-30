from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class PPP_without_HDLC(Base):
    __slots__ = ()
    _SDM_NAME = 'pppWithoutHDLC'
    _SDM_ATT_MAP = {
        'PPP Protocol Type': 'ppp_no_hdlc.header.protocolType',
    }

    def __init__(self, parent):
        super(PPP_without_HDLC, self).__init__(parent)

    @property
    def PPP_Protocol_Type(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PPP Protocol Type']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
