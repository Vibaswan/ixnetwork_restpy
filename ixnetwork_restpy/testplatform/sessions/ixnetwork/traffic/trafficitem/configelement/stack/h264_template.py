from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class H264(Base):
    __slots__ = ()
    _SDM_NAME = 'h264'
    _SDM_ATT_MAP = {
        'Version': 'h264.header.Version',
        'Padding Bit': 'h264.header.paddingBit',
        'Extension Bit': 'h264.header.extensionBit',
        'CSRC Count': 'h264.header.csrcCount',
        'Marker': 'h264.header.Marker',
        'Payload Type': 'h264.header.payloadType',
        'Sequence Number': 'h264.header.sequenceNumber',
        'Timestamp': 'h264.header.timestamp',
        'SSRC': 'h264.header.synchronizationSourceIdentifier',
    }

    def __init__(self, parent):
        super(H264, self).__init__(parent)

    @property
    def Version(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Version']))

    @property
    def Padding_Bit(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Padding Bit']))

    @property
    def Extension_Bit(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Extension Bit']))

    @property
    def CSRC_Count(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CSRC Count']))

    @property
    def Marker(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Marker']))

    @property
    def Payload_Type(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Payload Type']))

    @property
    def Sequence_Number(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Sequence Number']))

    @property
    def Timestamp(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Timestamp']))

    @property
    def SSRC(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SSRC']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
