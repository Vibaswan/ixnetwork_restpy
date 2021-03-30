from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class VPLS_Ethernet_Frame(Base):
    __slots__ = ()
    _SDM_NAME = 'vplsEthernet'
    _SDM_ATT_MAP = {
        'CW Zero': 'vplsEthernet.pweControlWord.zero',
        'CW Rsvd': 'vplsEthernet.pweControlWord.reserved',
        'CW Sequence Number': 'vplsEthernet.pweControlWord.sequenceNumber',
    }

    def __init__(self, parent):
        super(VPLS_Ethernet_Frame, self).__init__(parent)

    @property
    def CW_Zero(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CW Zero']))

    @property
    def CW_Rsvd(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CW Rsvd']))

    @property
    def CW_Sequence_Number(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CW Sequence Number']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
