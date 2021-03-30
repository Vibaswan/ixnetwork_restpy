from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class eCPRI(Base):
    __slots__ = ()
    _SDM_NAME = 'eCpri'
    _SDM_ATT_MAP = {
        'Protocol Revision': 'eCpri.commonheader.protocolRevision',
        'Reserved': 'eCpri.commonheader.reserved',
        'Concatenation': 'eCpri.commonheader.concatenation',
        'Message Type': 'eCpri.commonheader.messageType',
        'Payload Size (octets)': 'eCpri.commonheader.payloadSize',
    }

    def __init__(self, parent):
        super(eCPRI, self).__init__(parent)

    @property
    def Protocol_Revision(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Protocol Revision']))

    @property
    def Reserved(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Reserved']))

    @property
    def Concatenation(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Concatenation']))

    @property
    def Message_Type(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Message Type']))

    @property
    def Payload_Size_octets(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Payload Size (octets)']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
