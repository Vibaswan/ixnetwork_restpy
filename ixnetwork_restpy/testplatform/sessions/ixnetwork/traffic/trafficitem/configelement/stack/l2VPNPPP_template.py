from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class L2VPN_PPP(Base):
    __slots__ = ()
    _SDM_NAME = 'l2VPNPPP'
    _SDM_ATT_MAP = {
        'Address': 'l2VPNPPP.pppHeader.address',
        'Control': 'l2VPNPPP.pppHeader.control',
        'Protocol Type': 'l2VPNPPP.pppHeader.protocolType',
    }

    def __init__(self, parent):
        super(L2VPN_PPP, self).__init__(parent)

    @property
    def Address(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Address']))

    @property
    def Control(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Control']))

    @property
    def Protocol_Type(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Protocol Type']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
