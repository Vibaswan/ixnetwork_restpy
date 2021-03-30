from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class LDP_Keep_Alive_Message(Base):
    __slots__ = ()
    _SDM_NAME = 'ldpKeepAlive'
    _SDM_ATT_MAP = {
        'Version': 'ldpKeepAlive.header.version',
        'PDU length(in octets)': 'ldpKeepAlive.header.pduLengthinOctets',
        'LSR ID': 'ldpKeepAlive.header.lsrID',
        'Label space': 'ldpKeepAlive.header.labelSpace',
        'U bit': 'ldpKeepAlive.header.uBit',
        'Type': 'ldpKeepAlive.header.type',
        'Length': 'ldpKeepAlive.header.length',
        'Message ID': 'ldpKeepAlive.header.messageID',
    }

    def __init__(self, parent):
        super(LDP_Keep_Alive_Message, self).__init__(parent)

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

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
