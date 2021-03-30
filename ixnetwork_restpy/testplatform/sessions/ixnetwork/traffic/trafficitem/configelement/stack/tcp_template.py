from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class TCP(Base):
    __slots__ = ()
    _SDM_NAME = 'tcp'
    _SDM_ATT_MAP = {
        'TCP-Source-Port': 'tcp.header.srcPort-1',
        'TCP-Dest-Port': 'tcp.header.dstPort-2',
        'Sequence Number': 'tcp.header.sequenceNumber-3',
        'Acknowledgement Number': 'tcp.header.acknowledgementNumber-4',
        'Data Offset': 'tcp.header.dataOffset-5',
        'Reserved': 'tcp.header.reserved',
        'ECN': 'tcp.header.ecn',
        'Control Bits': 'tcp.header.controlBits',
        'Window': 'tcp.header.window',
        'TCP-Checksum': 'tcp.header.checksum',
        'Urgent Pointer': 'tcp.header.urgentPtr',
        'TCP-Options': 'tcp.header.options',
    }

    def __init__(self, parent):
        super(TCP, self).__init__(parent)

    @property
    def TCP_Source_Port(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TCP-Source-Port']))

    @property
    def TCP_Dest_Port(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TCP-Dest-Port']))

    @property
    def Sequence_Number(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Sequence Number']))

    @property
    def Acknowledgement_Number(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Acknowledgement Number']))

    @property
    def Data_Offset(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Data Offset']))

    @property
    def Reserved(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Reserved']))

    @property
    def ECN(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ECN']))

    @property
    def Control_Bits(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Control Bits']))

    @property
    def Window(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Window']))

    @property
    def TCP_Checksum(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TCP-Checksum']))

    @property
    def Urgent_Pointer(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Urgent Pointer']))

    @property
    def TCP_Options(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TCP-Options']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
