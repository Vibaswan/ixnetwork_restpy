from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class IPv6_Hop_by_Hop_Options_With_IOAM_Header(Base):
    __slots__ = ()
    _SDM_NAME = 'ipv6HopByHopOptionsWithIOAM'
    _SDM_ATT_MAP = {
        'IPv6 Hop-by-Hop Options Header': 'ipv6HopByHopOptionsWithIOAM.header.hopByHopOptionsHeader',
        'Padding': 'ipv6HopByHopOptionsWithIOAM.header.pad',
    }

    def __init__(self, parent):
        super(IPv6_Hop_by_Hop_Options_With_IOAM_Header, self).__init__(parent)

    @property
    def IPv6_Hop_by_Hop_Options_Header(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IPv6 Hop-by-Hop Options Header']))

    @property
    def Padding(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Padding']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
