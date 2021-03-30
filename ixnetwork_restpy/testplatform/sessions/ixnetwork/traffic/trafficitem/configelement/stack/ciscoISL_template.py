from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Cisco_ISL(Base):
    __slots__ = ()
    _SDM_NAME = 'ciscoISL'
    _SDM_ATT_MAP = {
        'Destination address': 'ciscoISL.header.dstAddress',
        'Frame type': 'ciscoISL.header.frameType',
        'User defined bits': 'ciscoISL.header.userBits',
        'Source address - high 24 bits': 'ciscoISL.header.srcAddressHi24',
        'Source address - low 24 bits': 'ciscoISL.header.srcAddressLo24',
        'Length': 'ciscoISL.header.length',
        'SNAP / LLC': 'ciscoISL.header.snapLLC',
        'High bits of Source Address': 'ciscoISL.header.hiBitsOfSrcAddress',
        'Destination VLAN': 'ciscoISL.header.dstVlan',
        'BPDU and CDP indicator': 'ciscoISL.header.bpduCDP',
        'Index': 'ciscoISL.header.index',
        'Reserved for Token Ring and FDDI': 'ciscoISL.header.reserved',
    }

    def __init__(self, parent):
        super(Cisco_ISL, self).__init__(parent)

    @property
    def Destination_address(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Destination address']))

    @property
    def Frame_type(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Frame type']))

    @property
    def User_defined_bits(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['User defined bits']))

    @property
    def Source_address___high_24_bits(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Source address - high 24 bits']))

    @property
    def Source_address___low_24_bits(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Source address - low 24 bits']))

    @property
    def Length(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Length']))

    @property
    def SNAP___LLC(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SNAP / LLC']))

    @property
    def High_bits_of_Source_Address(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['High bits of Source Address']))

    @property
    def Destination_VLAN(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Destination VLAN']))

    @property
    def BPDU_and_CDP_indicator(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BPDU and CDP indicator']))

    @property
    def Index(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Index']))

    @property
    def Reserved_for_Token_Ring_and_FDDI(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Reserved for Token Ring and FDDI']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
