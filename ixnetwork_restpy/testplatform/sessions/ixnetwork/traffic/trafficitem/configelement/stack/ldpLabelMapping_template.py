from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class LDP_Label_Mapping_Message(Base):
    __slots__ = ()
    _SDM_NAME = 'ldpLabelMapping'
    _SDM_ATT_MAP = {
        'Version': 'ldpLabelMapping.header.version',
        'PDU length(in octets)': 'ldpLabelMapping.header.pduLengthinOctets',
        'LSR ID': 'ldpLabelMapping.header.lsrID',
        'Label space': 'ldpLabelMapping.header.labelSpace',
        'U bit': 'ldpLabelMapping.header.uBit',
        'Type': 'ldpLabelMapping.header.type',
        'Length': 'ldpLabelMapping.header.length',
        'Message ID': 'ldpLabelMapping.header.messageID',
        'FEC TLV': 'ldpLabelMapping.header.fecTLV',
        'Label TLV': 'ldpLabelMapping.header.labelTLV',
        'Optional LDP MP Status TLV': 'ldpLabelMapping.header.tclOptionalLDPMpStatusTLV',
        'Optional parameter': 'ldpLabelMapping.header.optionalParameter',
    }

    def __init__(self, parent):
        super(LDP_Label_Mapping_Message, self).__init__(parent)

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

    @property
    def Optional_LDP_MP_Status_TLV(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Optional LDP MP Status TLV']))

    @property
    def Optional_parameter(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Optional parameter']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
