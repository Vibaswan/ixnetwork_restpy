from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class IPv6_Routing_Header_Type_4(Base):
    __slots__ = ()
    _SDM_NAME = 'ipv6RoutingType4'
    _SDM_ATT_MAP = {
        'Next Header': 'ipv6RoutingType4.segmentRoutingHeader.nextHeader',
        'Hdr Ext Len': 'ipv6RoutingType4.segmentRoutingHeader.hdrExtLen',
        'Routing Type': 'ipv6RoutingType4.segmentRoutingHeader.routingType',
        'Segments Left': 'ipv6RoutingType4.segmentRoutingHeader.segmentsLeft',
        'Last Entry': 'ipv6RoutingType4.segmentRoutingHeader.lastEntry',
        'Flags': 'ipv6RoutingType4.segmentRoutingHeader.flags',
        'Tag': 'ipv6RoutingType4.segmentRoutingHeader.tag',
        'Segment List': 'ipv6RoutingType4.segmentRoutingHeader.segmentList',
        'SR-IPv6 TLV List': 'ipv6RoutingType4.segmentRoutingHeader.srhTLVs',
    }

    def __init__(self, parent):
        super(IPv6_Routing_Header_Type_4, self).__init__(parent)

    @property
    def Next_Header(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Next Header']))

    @property
    def Hdr_Ext_Len(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Hdr Ext Len']))

    @property
    def Routing_Type(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Routing Type']))

    @property
    def Segments_Left(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Segments Left']))

    @property
    def Last_Entry(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Last Entry']))

    @property
    def Flags(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Flags']))

    @property
    def Tag(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Tag']))

    @property
    def Segment_List(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Segment List']))

    @property
    def SR_IPv6_TLV_List(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SR-IPv6 TLV List']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
