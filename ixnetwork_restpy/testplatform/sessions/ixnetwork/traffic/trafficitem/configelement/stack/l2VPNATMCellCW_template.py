from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class L2VPN_ATM_Cell_CW(Base):
    __slots__ = ()
    _SDM_NAME = 'l2VPNATMCellCW'
    _SDM_ATT_MAP = {
        'CW RSVD': 'l2VPNATMCellCW.controlWord.reserved',
        'CW T Bit': 'l2VPNATMCellCW.controlWord.tbit',
        'CW E bit': 'l2VPNATMCellCW.controlWord.ebit',
        'CW L bit': 'l2VPNATMCellCW.controlWord.lbit',
        'CW C bit': 'l2VPNATMCellCW.controlWord.cbit',
        'CW Zero': 'l2VPNATMCellCW.controlWord.zero',
        'CW Length': 'l2VPNATMCellCW.controlWord.length',
        'CW Sequence Number': 'l2VPNATMCellCW.controlWord.sequenceNumber',
    }

    def __init__(self, parent):
        super(L2VPN_ATM_Cell_CW, self).__init__(parent)

    @property
    def CW_RSVD(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CW RSVD']))

    @property
    def CW_T_Bit(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CW T Bit']))

    @property
    def CW_E_bit(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CW E bit']))

    @property
    def CW_L_bit(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CW L bit']))

    @property
    def CW_C_bit(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CW C bit']))

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
