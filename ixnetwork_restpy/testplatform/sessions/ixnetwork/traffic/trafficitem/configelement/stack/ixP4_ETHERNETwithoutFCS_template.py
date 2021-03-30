from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class IxP4_ETHERNET_without_FCS(Base):
    __slots__ = ()
    _SDM_NAME = 'ixP4_ETHERNETwithoutFCS'
    _SDM_ATT_MAP = {
        'dstAddr': 'ixP4_ETHERNETwithoutFCS.eTHERNETwithoutFCS.dstAddr',
        'srcAddr': 'ixP4_ETHERNETwithoutFCS.eTHERNETwithoutFCS.srcAddr',
        'etherType': 'ixP4_ETHERNETwithoutFCS.eTHERNETwithoutFCS.etherType',
    }

    def __init__(self, parent):
        super(IxP4_ETHERNET_without_FCS, self).__init__(parent)

    @property
    def dstAddr(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['dstAddr']))

    @property
    def srcAddr(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['srcAddr']))

    @property
    def etherType(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['etherType']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
