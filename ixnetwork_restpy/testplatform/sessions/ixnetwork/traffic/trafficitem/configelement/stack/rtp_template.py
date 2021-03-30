from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class RTP(Base):
    __slots__ = ()
    _SDM_NAME = 'rtp'
    _SDM_ATT_MAP = {
        'Version': 'rtp.header.version',
        'Padding': 'rtp.header.pad',
        'Extension Bit': 'rtp.header.extensionBit',
        'Contributing source count': 'rtp.header.contributingSrcCount',
        'Marker Bit': 'rtp.header.markerBit',
        'Payload Type': 'rtp.header.payloadType',
        'Sequence Number': 'rtp.header.sequenceNumber',
        'Timestamp': 'rtp.header.timestamp',
        'Synchronization source': 'rtp.header.synchronizationSource',
        'Next contributing source': 'rtp.header.nextContributingSource',
        'Header extension': 'rtp.header.headerExtension',
    }

    def __init__(self, parent):
        super(RTP, self).__init__(parent)

    @property
    def Version(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Version']))

    @property
    def Padding(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Padding']))

    @property
    def Extension_Bit(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Extension Bit']))

    @property
    def Contributing_source_count(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Contributing source count']))

    @property
    def Marker_Bit(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Marker Bit']))

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
    def Synchronization_source(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Synchronization source']))

    @property
    def Next_contributing_source(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Next contributing source']))

    @property
    def Header_extension(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Header extension']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
