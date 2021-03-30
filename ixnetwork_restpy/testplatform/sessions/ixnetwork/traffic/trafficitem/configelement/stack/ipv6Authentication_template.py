from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class IPv6_Authentication_Header(Base):
    __slots__ = ()
    _SDM_NAME = 'ipv6Authentication'
    _SDM_ATT_MAP = {
        'Ipv6 Authentication Header': 'ipv6Authentication.header.authenticationHeader',
        'Padding': 'ipv6Authentication.header.pad',
    }

    def __init__(self, parent):
        super(IPv6_Authentication_Header, self).__init__(parent)

    @property
    def Ipv6_Authentication_Header(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Ipv6 Authentication Header']))

    @property
    def Padding(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Padding']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
