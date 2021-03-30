from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class RTCP(Base):
    __slots__ = ()
    _SDM_NAME = 'realTimeTransportControlProtocol'
    _SDM_ATT_MAP = {
        'RTCP header': 'realTimeTransportControlProtocol.header.rtcpHeader',
        'Sender Report header': 'realTimeTransportControlProtocol.header.senderReportHeader',
        'Receiver Report Header': 'realTimeTransportControlProtocol.header.receiverReportHeader',
        'Source Description(SDES) Packet': 'realTimeTransportControlProtocol.header.sourceDescriptionPacket',
        'BYE Packet': 'realTimeTransportControlProtocol.header.byePacket',
        'Application Defined Packet': 'realTimeTransportControlProtocol.header.applicationDefinedPacket',
    }

    def __init__(self, parent):
        super(RTCP, self).__init__(parent)

    @property
    def RTCP_header(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RTCP header']))

    @property
    def Sender_Report_header(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Sender Report header']))

    @property
    def Receiver_Report_Header(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Receiver Report Header']))

    @property
    def Source_DescriptionSDES_Packet(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Source Description(SDES) Packet']))

    @property
    def BYE_Packet(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BYE Packet']))

    @property
    def Application_Defined_Packet(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Application Defined Packet']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
