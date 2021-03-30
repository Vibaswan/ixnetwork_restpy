from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class ICMP_Msg_Types__0_8_13_14_15_16(Base):
    __slots__ = ()
    _SDM_NAME = 'icmpv2'
    _SDM_ATT_MAP = {
        'Message type': 'icmpv2.message.messageType',
        'Code value': 'icmpv2.message.codeValue',
        'ICMP checksum': 'icmpv2.message.icmpChecksum',
        'Identifier': 'icmpv2.message.identifier',
        'Sequence number': 'icmpv2.message.sequenceNumber',
        'Next Fields': 'icmpv2.message.nextFields',
    }

    def __init__(self, parent):
        super(ICMP_Msg_Types__0_8_13_14_15_16, self).__init__(parent)

    @property
    def Message_type(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Message type']))

    @property
    def Code_value(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Code value']))

    @property
    def ICMP_checksum(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ICMP checksum']))

    @property
    def Identifier(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Identifier']))

    @property
    def Sequence_number(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Sequence number']))

    @property
    def Next_Fields(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Next Fields']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
