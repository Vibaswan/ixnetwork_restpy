from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class IPv4(Base):
    __slots__ = ()
    _SDM_NAME = 'ipv4'
    _SDM_ATT_MAP = {
        'Version': 'ipv4.header.version-1',
        'Header Length': 'ipv4.header.headerLength-2',
        'IP Priority': 'ipv4.header.priority-3',
        'Total Length (octets)': 'ipv4.header.totalLength-4',
        'Identification': 'ipv4.header.identification-19',
        'Flags': 'ipv4.header.flags-6',
        'Fragment offset': 'ipv4.header.fragmentOffset-23',
        'TTL (Time to live)': 'ipv4.header.ttl-24',
        'Protocol': 'ipv4.header.protocol-9',
        'Header checksum': 'ipv4.header.checksum-10',
        'Source Address': 'ipv4.header.srcIp-27',
        'Destination Address': 'ipv4.header.dstIp-28',
        'IP options': 'ipv4.header.options-13',
    }

    def __init__(self, parent):
        super(IPv4, self).__init__(parent)

    @property
    def Version(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Version']))

    @property
    def Header_Length(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Header Length']))

    @property
    def IP_Priority(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IP Priority']))

    @property
    def Total_Length_octets(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Total Length (octets)']))

    @property
    def Identification(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Identification']))

    @property
    def Flags(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Flags']))

    @property
    def Fragment_offset(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Fragment offset']))

    @property
    def TTL_Time_to_live(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TTL (Time to live)']))

    @property
    def Protocol(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Protocol']))

    @property
    def Header_checksum(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Header checksum']))

    @property
    def Source_Address(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Source Address']))

    @property
    def Destination_Address(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Destination Address']))

    @property
    def IP_options(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IP options']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
