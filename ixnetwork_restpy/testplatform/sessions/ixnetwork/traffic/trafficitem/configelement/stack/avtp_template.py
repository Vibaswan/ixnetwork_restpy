from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class AVTP(Base):
    __slots__ = ()
    _SDM_NAME = 'avtp'
    _SDM_ATT_MAP = {
        'AVTP Common Header': 'avtp.header.avtpCommonHeader',
        'AVTP Type Specific Header': 'avtp.header.avtpTypeSpecificHeader',
        'SRP Stream ID': 'avtp.header.srpStreamId',
        'Packet Information': 'avtp.header.packetInformation',
    }

    def __init__(self, parent):
        super(AVTP, self).__init__(parent)

    @property
    def AVTP_Common_Header(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AVTP Common Header']))

    @property
    def AVTP_Type_Specific_Header(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AVTP Type Specific Header']))

    @property
    def SRP_Stream_ID(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SRP Stream ID']))

    @property
    def Packet_Information(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Packet Information']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
