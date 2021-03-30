from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class L2VPN_FR_CW(Base):
    __slots__ = ()
    _SDM_NAME = 'l2VPNFrameRelayCW'
    _SDM_ATT_MAP = {
        'CW Rsvd': 'l2VPNFrameRelayCW.controlWord.reserved',
        'CW B Bit': 'l2VPNFrameRelayCW.controlWord.bbit',
        'CW F Bit': 'l2VPNFrameRelayCW.controlWord.fbit',
        'CW D Bit': 'l2VPNFrameRelayCW.controlWord.dbit',
        'CW C Bit': 'l2VPNFrameRelayCW.controlWord.cbit',
        'CW Zero': 'l2VPNFrameRelayCW.controlWord.zero',
        'CW Length': 'l2VPNFrameRelayCW.controlWord.length',
        'CW Sequence Number': 'l2VPNFrameRelayCW.controlWord.sequenceNumber',
    }

    def __init__(self, parent):
        super(L2VPN_FR_CW, self).__init__(parent)

    @property
    def CW_Rsvd(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CW Rsvd']))

    @property
    def CW_B_Bit(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CW B Bit']))

    @property
    def CW_F_Bit(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CW F Bit']))

    @property
    def CW_D_Bit(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CW D Bit']))

    @property
    def CW_C_Bit(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CW C Bit']))

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
