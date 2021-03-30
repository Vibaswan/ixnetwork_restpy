from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class MAC_in_MAC_v42(Base):
    __slots__ = ()
    _SDM_NAME = 'macInMACv42'
    _SDM_ATT_MAP = {
        'B-Destination Address (Ethernet)': 'macInMACv42.header.bDstAddress',
        'B-Source Address (Ethernet)': 'macInMACv42.header.bSrcAddress',
        'B-TAG Ethertype': 'macInMACv42.header.bTAGEthertype',
        'I-TAG Ethertype': 'macInMACv42.header.iTAGEthertype',
        'C-Destination Address (Ethernet)': 'macInMACv42.header.cDstAddress',
        'C-Source Address (Ethernet)': 'macInMACv42.header.cSrcAddress',
        'Add S-TAG/C-TAG': 'macInMACv42.header.sTAGCTAG',
    }

    def __init__(self, parent):
        super(MAC_in_MAC_v42, self).__init__(parent)

    @property
    def B_Destination_Address_Ethernet(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['B-Destination Address (Ethernet)']))

    @property
    def B_Source_Address_Ethernet(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['B-Source Address (Ethernet)']))

    @property
    def B_TAG_Ethertype(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['B-TAG Ethertype']))

    @property
    def I_TAG_Ethertype(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['I-TAG Ethertype']))

    @property
    def C_Destination_Address_Ethernet(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['C-Destination Address (Ethernet)']))

    @property
    def C_Source_Address_Ethernet(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['C-Source Address (Ethernet)']))

    @property
    def Add_S_TAG_C_TAG(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Add S-TAG/C-TAG']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
