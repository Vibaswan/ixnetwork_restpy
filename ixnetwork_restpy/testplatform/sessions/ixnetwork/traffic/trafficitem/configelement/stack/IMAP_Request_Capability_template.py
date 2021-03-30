from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class IMAP_Request_Capability(Base):
    __slots__ = ()
    _SDM_NAME = 'IMAP_Request_Capability'
    _SDM_ATT_MAP = {
        'Request Tag': 'IMAP_Request_Capability.REQUEST.Request Tag',
        'SP': 'IMAP_Request_Capability.REQUEST.SP',
        'Request': 'IMAP_Request_Capability.REQUEST.Request',
        'CRLF': 'IMAP_Request_Capability.REQUEST.CRLF',
    }

    def __init__(self, parent):
        super(IMAP_Request_Capability, self).__init__(parent)

    @property
    def Request_Tag(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Request Tag']))

    @property
    def SP(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SP']))

    @property
    def Request(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Request']))

    @property
    def CRLF(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CRLF']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
