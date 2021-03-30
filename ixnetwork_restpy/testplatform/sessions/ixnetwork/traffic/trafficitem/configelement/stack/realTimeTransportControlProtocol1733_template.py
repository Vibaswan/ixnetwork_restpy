from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class RTCP_1733(Base):
    __slots__ = ()
    _SDM_NAME = 'realTimeTransportControlProtocol1733'
    _SDM_ATT_MAP = {
        'Version': 'realTimeTransportControlProtocol1733.rtcpHeader.version',
        'Padding': 'realTimeTransportControlProtocol1733.rtcpHeader.paddingBit',
        'Subtype': 'realTimeTransportControlProtocol1733.rtcpHeader.subtype',
        'Packet Type': 'realTimeTransportControlProtocol1733.rtcpHeader.packetType',
        'Message Length': 'realTimeTransportControlProtocol1733.rtcpHeader.messageLength',
        'SSRC/CSRC': 'realTimeTransportControlProtocol1733.rtcpHeader.ssrc/csrc',
        'Name': 'realTimeTransportControlProtocol1733.rtcpHeader.name',
        'gm Time Base Indicator': 'realTimeTransportControlProtocol1733.rtcpHeader.gmTimeBaseIndicator',
        'gm Identity': 'realTimeTransportControlProtocol1733.rtcpHeader.gmIdentity',
        'Stream Id': 'realTimeTransportControlProtocol1733.rtcpHeader.stream_id',
        'As Timestamp': 'realTimeTransportControlProtocol1733.rtcpHeader.asTimestamp',
        'RTP Timestamp': 'realTimeTransportControlProtocol1733.rtcpHeader.rtpTimestamp',
    }

    def __init__(self, parent):
        super(RTCP_1733, self).__init__(parent)

    @property
    def Version(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Version']))

    @property
    def Padding(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Padding']))

    @property
    def Subtype(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Subtype']))

    @property
    def Packet_Type(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Packet Type']))

    @property
    def Message_Length(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Message Length']))

    @property
    def SSRC_CSRC(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SSRC/CSRC']))

    @property
    def Name(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Name']))

    @property
    def gm_Time_Base_Indicator(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['gm Time Base Indicator']))

    @property
    def gm_Identity(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['gm Identity']))

    @property
    def Stream_Id(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Stream Id']))

    @property
    def As_Timestamp(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['As Timestamp']))

    @property
    def RTP_Timestamp(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RTP Timestamp']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
