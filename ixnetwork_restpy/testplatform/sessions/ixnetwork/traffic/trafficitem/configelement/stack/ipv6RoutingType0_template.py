from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class IPv6_Routing_Header_Type_0(Base):
    __slots__ = ()
    _SDM_NAME = 'ipv6RoutingType0'
    _SDM_ATT_MAP = {
        'Next Header': 'ipv6RoutingType0.routingHeaderType0.nextHeader',
        'Header Extension Length (8 octets)': 'ipv6RoutingType0.routingHeaderType0.headerExtensionLength',
        'Routing Type': 'ipv6RoutingType0.routingHeaderType0.routingType',
        'Segments Left': 'ipv6RoutingType0.routingHeaderType0.segmentsLeft',
        'Reserved': 'ipv6RoutingType0.routingHeaderType0.reserved',
        'Addresses': 'ipv6RoutingType0.routingHeaderType0.addresses',
    }

    def __init__(self, parent):
        super(IPv6_Routing_Header_Type_0, self).__init__(parent)

    @property
    def Next_Header(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Next Header']))

    @property
    def Header_Extension_Length_8_octets(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Header Extension Length (8 octets)']))

    @property
    def Routing_Type(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Routing Type']))

    @property
    def Segments_Left(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Segments Left']))

    @property
    def Reserved(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Reserved']))

    @property
    def Addresses(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Addresses']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
