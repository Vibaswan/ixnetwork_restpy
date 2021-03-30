from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class LDP_Notification_Message(Base):
    __slots__ = ()
    _SDM_NAME = 'ldpNotification'
    _SDM_ATT_MAP = {
        'Version': 'ldpNotification.header.version',
        'PDU length(in octets)': 'ldpNotification.header.pduLengthinOctets',
        'LSR ID': 'ldpNotification.header.lsrID',
        'Label space': 'ldpNotification.header.labelSpace',
        'U bit': 'ldpNotification.header.uBit',
        'Type': 'ldpNotification.header.type',
        'Length': 'ldpNotification.header.length',
        'Message ID': 'ldpNotification.header.messageID',
        'Status TLV': 'ldpNotification.header.statusTLV',
        'LDP MP Status TLV': 'ldpNotification.header.tclLDPMpStatusTLV',
        'Optional LDP MP FEC TLV': 'ldpNotification.header.fecTLV',
        'Optional Label TLV': 'ldpNotification.header.labelTLV',
        'Optional parameter': 'ldpNotification.header.optionalParameter',
    }

    def __init__(self, parent):
        super(LDP_Notification_Message, self).__init__(parent)

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
    def Status_TLV(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Status TLV']))

    @property
    def LDP_MP_Status_TLV(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LDP MP Status TLV']))

    @property
    def Optional_LDP_MP_FEC_TLV(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Optional LDP MP FEC TLV']))

    @property
    def Optional_Label_TLV(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Optional Label TLV']))

    @property
    def Optional_parameter(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Optional parameter']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
