from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class LLDP(Base):
    __slots__ = ()
    _SDM_NAME = 'lldp'
    _SDM_ATT_MAP = {
        'Mandatory TLVs': 'lldp.header.mandatoryTlv',
        'Optional TLVs': 'lldp.header.optionalTlvs',
        'Organizationally Specific TLVs': 'lldp.header.organizationalTlvs',
        'End Of LLDPDU TLV': 'lldp.header.endLldpTlv',
    }

    def __init__(self, parent):
        super(LLDP, self).__init__(parent)

    @property
    def Mandatory_TLVs(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Mandatory TLVs']))

    @property
    def Optional_TLVs(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Optional TLVs']))

    @property
    def Organizationally_Specific_TLVs(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Organizationally Specific TLVs']))

    @property
    def End_Of_LLDPDU_TLV(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['End Of LLDPDU TLV']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
