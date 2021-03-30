from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class LDP_Initialization_Message(Base):
    __slots__ = ()
    _SDM_NAME = 'ldpInitialization'
    _SDM_ATT_MAP = {
        'Version': 'ldpInitialization.header.version',
        'PDU length(in octets)': 'ldpInitialization.header.pduLengthinOctets',
        'LSR ID': 'ldpInitialization.header.lsrID',
        'Label space': 'ldpInitialization.header.labelSpace',
        'U bit': 'ldpInitialization.header.uBit',
        'Type': 'ldpInitialization.header.type',
        'Length': 'ldpInitialization.header.length',
        'Message ID': 'ldpInitialization.header.messageID',
        'Common session parameters TLV': 'ldpInitialization.header.commonSessionParametersTLV',
        'Optional parameter': 'ldpInitialization.header.optionalParameter',
    }

    def __init__(self, parent):
        super(LDP_Initialization_Message, self).__init__(parent)

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
    def Common_session_parameters_TLV(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Common session parameters TLV']))

    @property
    def Optional_parameter(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Optional parameter']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
