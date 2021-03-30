from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class T_MPLS_Ethernet_Unicast(Base):
    __slots__ = ()
    _SDM_NAME = 'tmpls'
    _SDM_ATT_MAP = {
        'TMP Label': 'tmpls.header.tmpLabel',
        'TMC Label': 'tmpls.header.tmcLabel',
        'C-Destination MAC Address': 'tmpls.header.cDstMAC',
        'C-Source MAC Address': 'tmpls.header.cSrcMAC',
    }

    def __init__(self, parent):
        super(T_MPLS_Ethernet_Unicast, self).__init__(parent)

    @property
    def TMP_Label(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TMP Label']))

    @property
    def TMC_Label(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TMC Label']))

    @property
    def C_Destination_MAC_Address(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['C-Destination MAC Address']))

    @property
    def C_Source_MAC_Address(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['C-Source MAC Address']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
