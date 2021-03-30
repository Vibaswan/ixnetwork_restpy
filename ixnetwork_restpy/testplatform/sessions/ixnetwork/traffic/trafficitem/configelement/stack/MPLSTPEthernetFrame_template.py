from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class MPLS_TP_Ethernet_Frame(Base):
    __slots__ = ()
    _SDM_NAME = 'MPLSTPEthernetFrame'
    _SDM_ATT_MAP = {
        'CW Rsvd': 'MPLSTPEthernetFrame.controlWord.reserved',
        'CW Flags': 'MPLSTPEthernetFrame.controlWord.flags',
        'CW Zero': 'MPLSTPEthernetFrame.controlWord.zero',
        'CW Length': 'MPLSTPEthernetFrame.controlWord.length',
        'CW Sequence Number': 'MPLSTPEthernetFrame.controlWord.sequenceNumber',
    }

    def __init__(self, parent):
        super(MPLS_TP_Ethernet_Frame, self).__init__(parent)

    @property
    def CW_Rsvd(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CW Rsvd']))

    @property
    def CW_Flags(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CW Flags']))

    @property
    def CW_Zero(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CW Zero']))

    @property
    def CW_Length(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CW Length']))

    @property
    def CW_Sequence_Number(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CW Sequence Number']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
