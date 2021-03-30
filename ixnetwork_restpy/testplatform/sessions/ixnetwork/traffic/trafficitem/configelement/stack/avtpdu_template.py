from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class AVTP_17221(Base):
    __slots__ = ()
    _SDM_NAME = 'avtpdu'
    _SDM_ATT_MAP = {
        'AVTPDU Common Stream Header': 'avtpdu.header.avtpduCommonStreamHeader',
        'AVTPDU Type Specific Header': 'avtpdu.header.avtpduTypeSpecificHeader',
        'AVTPDU Stream ID': 'avtpdu.header.avtpduStreamId',
        'Select Initial Part': 'avtpdu.header.selectInitialPart',
        'Packet Information': 'avtpdu.header.packetInformation',
    }

    def __init__(self, parent):
        super(AVTP_17221, self).__init__(parent)

    @property
    def AVTPDU_Common_Stream_Header(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AVTPDU Common Stream Header']))

    @property
    def AVTPDU_Type_Specific_Header(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AVTPDU Type Specific Header']))

    @property
    def AVTPDU_Stream_ID(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AVTPDU Stream ID']))

    @property
    def Select_Initial_Part(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Select Initial Part']))

    @property
    def Packet_Information(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Packet Information']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
