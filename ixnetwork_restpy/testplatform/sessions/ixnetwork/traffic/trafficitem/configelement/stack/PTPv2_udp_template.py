from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class PTPv2___All_Messages(Base):
    __slots__ = ()
    _SDM_NAME = 'PTPv2_udp'
    _SDM_ATT_MAP = {
        'Header': 'PTPv2_udp.header.header',
        'Message Types': 'PTPv2_udp.header.messageTypes',
        'TLVs': 'PTPv2_udp.header.tlvs',
    }

    def __init__(self, parent):
        super(PTPv2___All_Messages, self).__init__(parent)

    @property
    def Header(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Header']))

    @property
    def Message_Types(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Message Types']))

    @property
    def TLVs(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TLVs']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
