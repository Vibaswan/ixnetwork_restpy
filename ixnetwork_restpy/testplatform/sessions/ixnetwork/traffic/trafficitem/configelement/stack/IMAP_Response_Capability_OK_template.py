from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class IMAP_Response_Capability_OK(Base):
    __slots__ = ()
    _SDM_NAME = 'IMAP_Response_Capability_OK'
    _SDM_ATT_MAP = {
        'RESPONSE1': 'IMAP_Response_Capability_OK.header.RESPONSE1',
        'RESPONSE2': 'IMAP_Response_Capability_OK.header.RESPONSE2',
    }

    def __init__(self, parent):
        super(IMAP_Response_Capability_OK, self).__init__(parent)

    @property
    def RESPONSE1(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RESPONSE1']))

    @property
    def RESPONSE2(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RESPONSE2']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
