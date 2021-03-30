from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class IPv6_Encapsulation_Header(Base):
    __slots__ = ()
    _SDM_NAME = 'ipv6Encapsulation'
    _SDM_ATT_MAP = {
        'Security Paramaters Index': 'ipv6Encapsulation.header.spi',
        'Sequence Number': 'ipv6Encapsulation.header.sequenceNumber',
    }

    def __init__(self, parent):
        super(IPv6_Encapsulation_Header, self).__init__(parent)

    @property
    def Security_Paramaters_Index(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Security Paramaters Index']))

    @property
    def Sequence_Number(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Sequence Number']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
