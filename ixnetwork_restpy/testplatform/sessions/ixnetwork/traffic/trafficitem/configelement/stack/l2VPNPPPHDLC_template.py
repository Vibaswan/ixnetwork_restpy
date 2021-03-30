from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class L2VPN_PPP_HDLC_Frame(Base):
    __slots__ = ()
    _SDM_NAME = 'l2VPNPPPHDLC'
    _SDM_ATT_MAP = {
        'CW Rsvd': 'l2VPNPPPHDLC.controlWord.reserved',
        'CW Flags': 'l2VPNPPPHDLC.controlWord.flags',
        'CW Zero': 'l2VPNPPPHDLC.controlWord.zero',
        'CW Length': 'l2VPNPPPHDLC.controlWord.length',
        'CW Sequence Number': 'l2VPNPPPHDLC.controlWord.sequenceNumber',
    }

    def __init__(self, parent):
        super(L2VPN_PPP_HDLC_Frame, self).__init__(parent)

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
