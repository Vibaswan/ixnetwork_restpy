from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class L2VPN_VC_Type_IP_CW(Base):
    __slots__ = ()
    _SDM_NAME = 'l2VPNVCTypeIPCW'
    _SDM_ATT_MAP = {
        'CW Rsvd': 'l2VPNVCTypeIPCW.controlWord.reserved',
        'CW Flags': 'l2VPNVCTypeIPCW.controlWord.flags',
        'CW FRG': 'l2VPNVCTypeIPCW.controlWord.zero',
        'CW Length': 'l2VPNVCTypeIPCW.controlWord.length',
        'CW Sequence Number': 'l2VPNVCTypeIPCW.controlWord.sequenceNumber',
    }

    def __init__(self, parent):
        super(L2VPN_VC_Type_IP_CW, self).__init__(parent)

    @property
    def CW_Rsvd(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CW Rsvd']))

    @property
    def CW_Flags(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CW Flags']))

    @property
    def CW_FRG(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CW FRG']))

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
