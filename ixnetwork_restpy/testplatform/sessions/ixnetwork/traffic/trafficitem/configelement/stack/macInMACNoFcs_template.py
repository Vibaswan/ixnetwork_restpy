from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class MAC_in_MAC_No_FCS(Base):
    __slots__ = ()
    _SDM_NAME = 'macInMACNoFcs'
    _SDM_ATT_MAP = {
        'B-Destination Address (Ethernet)': 'macInMACNoFcs.header.bdestinationAddressEthernet',
        'B-Source Address (Ethernet)': 'macInMACNoFcs.header.bsourceAddressEthernet',
        'B-Ethernet Type': 'macInMACNoFcs.header.bethernetType',
        'I-Tag EtherType': 'macInMACNoFcs.header.itagEtherType',
        'I-Tag': 'macInMACNoFcs.header.itag',
        'C-Destination Address (Ethernet)': 'macInMACNoFcs.header.cdestinationAddressEthernet',
        'C-Source Address (Ethernet)': 'macInMACNoFcs.header.csourceAddressEthernet',
        'S-Tag': 'macInMACNoFcs.header.stag',
        'C-Tag': 'macInMACNoFcs.header.ctag',
        'Type': 'macInMACNoFcs.header.type',
    }

    def __init__(self, parent):
        super(MAC_in_MAC_No_FCS, self).__init__(parent)

    @property
    def B_Destination_Address_Ethernet(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['B-Destination Address (Ethernet)']))

    @property
    def B_Source_Address_Ethernet(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['B-Source Address (Ethernet)']))

    @property
    def B_Ethernet_Type(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['B-Ethernet Type']))

    @property
    def I_Tag_EtherType(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['I-Tag EtherType']))

    @property
    def I_Tag(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['I-Tag']))

    @property
    def C_Destination_Address_Ethernet(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['C-Destination Address (Ethernet)']))

    @property
    def C_Source_Address_Ethernet(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['C-Source Address (Ethernet)']))

    @property
    def S_Tag(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['S-Tag']))

    @property
    def C_Tag(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['C-Tag']))

    @property
    def Type(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Type']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
