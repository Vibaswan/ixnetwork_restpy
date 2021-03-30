from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class LDP_Label_Abort_Request_Message(Base):
    __slots__ = ()
    _SDM_NAME = 'ldpLabelAbortRequest'
    _SDM_ATT_MAP = {
        'Version': 'ldpLabelAbortRequest.header.version',
        'PDU length(in octets)': 'ldpLabelAbortRequest.header.pduLengthinOctets',
        'LSR ID': 'ldpLabelAbortRequest.header.lsrID',
        'Label space': 'ldpLabelAbortRequest.header.labelSpace',
        'U bit': 'ldpLabelAbortRequest.header.uBit',
        'Type': 'ldpLabelAbortRequest.header.type',
        'Length': 'ldpLabelAbortRequest.header.length',
        'Message ID': 'ldpLabelAbortRequest.header.messageID',
        'FEC TLV': 'ldpLabelAbortRequest.header.fecTLV',
        'Label request message ID TLV': 'ldpLabelAbortRequest.header.labelRequestMessageIDTLV',
    }

    def __init__(self, parent):
        super(LDP_Label_Abort_Request_Message, self).__init__(parent)

    @property
    def Version(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Version']))

    @property
    def PDU_lengthin_octets(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PDU length(in octets)']))

    @property
    def LSR_ID(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LSR ID']))

    @property
    def Label_space(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Label space']))

    @property
    def U_bit(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['U bit']))

    @property
    def Type(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Type']))

    @property
    def Length(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Length']))

    @property
    def Message_ID(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Message ID']))

    @property
    def FEC_TLV(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FEC TLV']))

    @property
    def Label_request_message_ID_TLV(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Label request message ID TLV']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
