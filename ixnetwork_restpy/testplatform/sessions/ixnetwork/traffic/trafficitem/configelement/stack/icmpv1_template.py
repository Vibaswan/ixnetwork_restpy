from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class ICMP_Msg_Types__3_4_5_11_12(Base):
    __slots__ = ()
    _SDM_NAME = 'icmpv1'
    _SDM_ATT_MAP = {
        'Message type': 'icmpv1.message.messageType',
        'Code options': 'icmpv1.message.codeOptions',
        'ICMP checksum': 'icmpv1.message.icmpChecksum',
        'Next 4 bytes': 'icmpv1.message.next4Bytes',
    }

    def __init__(self, parent):
        super(ICMP_Msg_Types__3_4_5_11_12, self).__init__(parent)

    @property
    def Message_type(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Message type']))

    @property
    def Code_options(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Code options']))

    @property
    def ICMP_checksum(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ICMP checksum']))

    @property
    def Next_4_bytes(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Next 4 bytes']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
