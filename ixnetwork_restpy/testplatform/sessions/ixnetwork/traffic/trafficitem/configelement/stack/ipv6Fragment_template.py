from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class IPv6_Fragment_Header(Base):
    __slots__ = ()
    _SDM_NAME = 'ipv6Fragment'
    _SDM_ATT_MAP = {
        'Next Header': 'ipv6Fragment.fragmentHeader.nextHeader',
        'Reserved': 'ipv6Fragment.fragmentHeader.reserved1',
        'Fragment offset (8 octets)': 'ipv6Fragment.fragmentHeader.fragmentOffset',
        'Reserved': 'ipv6Fragment.fragmentHeader.reserved2',
        'More Fragments': 'ipv6Fragment.fragmentHeader.moreFragments',
        'Identification': 'ipv6Fragment.fragmentHeader.identification',
    }

    def __init__(self, parent):
        super(IPv6_Fragment_Header, self).__init__(parent)

    @property
    def Next_Header(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Next Header']))

    @property
    def Reserved(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Reserved']))

    @property
    def Fragment_offset_8_octets(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Fragment offset (8 octets)']))

    @property
    def Reserved(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Reserved']))

    @property
    def More_Fragments(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['More Fragments']))

    @property
    def Identification(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Identification']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
