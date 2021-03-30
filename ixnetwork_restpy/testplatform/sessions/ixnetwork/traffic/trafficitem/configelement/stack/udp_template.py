from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class UDP(Base):
    __slots__ = ()
    _SDM_NAME = 'udp'
    _SDM_ATT_MAP = {
        'UDP-Source-Port': 'udp.header.srcPort-1',
        'UDP-Dest-Port': 'udp.header.dstPort-2',
        'UDP-Length': 'udp.header.length-3',
        'UDP-Checksum': 'udp.header.checksum-4',
    }

    def __init__(self, parent):
        super(UDP, self).__init__(parent)

    @property
    def UDP_Source_Port(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['UDP-Source-Port']))

    @property
    def UDP_Dest_Port(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['UDP-Dest-Port']))

    @property
    def UDP_Length(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['UDP-Length']))

    @property
    def UDP_Checksum(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['UDP-Checksum']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
