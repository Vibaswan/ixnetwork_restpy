from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class IPv6_Routing_Header_Type_2(Base):
    __slots__ = ()
    _SDM_NAME = 'ipv6RoutingType2'
    _SDM_ATT_MAP = {
        'IPv6 Routing Header': 'ipv6RoutingType2.header.routingHeader',
        'Padding': 'ipv6RoutingType2.header.pad',
    }

    def __init__(self, parent):
        super(IPv6_Routing_Header_Type_2, self).__init__(parent)

    @property
    def IPv6_Routing_Header(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IPv6 Routing Header']))

    @property
    def Padding(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Padding']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
