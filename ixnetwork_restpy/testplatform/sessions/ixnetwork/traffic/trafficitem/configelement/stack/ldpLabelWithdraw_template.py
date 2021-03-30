from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class LDP_Label_Withdraw_Message(Base):
    __slots__ = ()
    _SDM_NAME = 'ldpLabelWithdraw'
    _SDM_ATT_MAP = {
        'Version': 'ldpLabelWithdraw.header.version',
        'PDU length(in octets)': 'ldpLabelWithdraw.header.pduLengthinOctets',
        'LSR ID': 'ldpLabelWithdraw.header.lsrID',
        'Label space': 'ldpLabelWithdraw.header.labelSpace',
        'U bit': 'ldpLabelWithdraw.header.uBit',
        'Type': 'ldpLabelWithdraw.header.type',
        'Length': 'ldpLabelWithdraw.header.length',
        'Message ID': 'ldpLabelWithdraw.header.messageID',
        'FEC TLV': 'ldpLabelWithdraw.header.fecTLV',
        'Label TLV': 'ldpLabelWithdraw.header.labelTLV',
    }

    def __init__(self, parent):
        super(LDP_Label_Withdraw_Message, self).__init__(parent)

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
    def Label_TLV(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Label TLV']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
