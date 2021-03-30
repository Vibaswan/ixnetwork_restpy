from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class OSPFv2_Hello_Packet(Base):
    __slots__ = ()
    _SDM_NAME = 'ospfv2Hello'
    _SDM_ATT_MAP = {
        'OSPFv2 Packet Header': 'ospfv2Hello.header.ospfv2PacketHeader',
        'Network mask': 'ospfv2Hello.header.networkMask',
        'Hello interval': 'ospfv2Hello.header.helloInterval',
        'Options': 'ospfv2Hello.header.options',
        'Router priority': 'ospfv2Hello.header.routerPriority',
        'Router dead interval': 'ospfv2Hello.header.routerDeadInterval',
        'Designated Router ID': 'ospfv2Hello.header.designatedRouterID',
        'Backup Designated Router ID': 'ospfv2Hello.header.backupDesignatedRouterID',
        'Hello Neighbor List': 'ospfv2Hello.header.helloNeighborList',
    }

    def __init__(self, parent):
        super(OSPFv2_Hello_Packet, self).__init__(parent)

    @property
    def OSPFv2_Packet_Header(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['OSPFv2 Packet Header']))

    @property
    def Network_mask(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Network mask']))

    @property
    def Hello_interval(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Hello interval']))

    @property
    def Options(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Options']))

    @property
    def Router_priority(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Router priority']))

    @property
    def Router_dead_interval(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Router dead interval']))

    @property
    def Designated_Router_ID(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Designated Router ID']))

    @property
    def Backup_Designated_Router_ID(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Backup Designated Router ID']))

    @property
    def Hello_Neighbor_List(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Hello Neighbor List']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
