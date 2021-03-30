from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class IPv6(Base):
    __slots__ = ()
    _SDM_NAME = 'ipv6'
    _SDM_ATT_MAP = {
        'Version, Traffic Class, Flow Label': 'ipv6.header.versionTrafficClassFlowLabel',
        'Payload Length': 'ipv6.header.payloadLength',
        'Next Header': 'ipv6.header.nextHeader',
        'Hop Limit': 'ipv6.header.hopLimit',
        'Source Address': 'ipv6.header.srcIP',
        'Destination Address': 'ipv6.header.dstIP',
    }

    def __init__(self, parent):
        super(IPv6, self).__init__(parent)

    @property
    def Version__Traffic_Class__Flow_Label(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Version, Traffic Class, Flow Label']))

    @property
    def Payload_Length(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Payload Length']))

    @property
    def Next_Header(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Next Header']))

    @property
    def Hop_Limit(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Hop Limit']))

    @property
    def Source_Address(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Source Address']))

    @property
    def Destination_Address(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Destination Address']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
