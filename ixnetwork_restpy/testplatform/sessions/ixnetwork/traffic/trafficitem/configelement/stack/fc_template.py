from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class FC(Base):
    __slots__ = ()
    _SDM_NAME = 'fc'
    _SDM_ATT_MAP = {
        'SOF': 'fc.fcHeader.sof',
        'R_CTL': 'fc.fcHeader.rCTL',
        'Destination ID': 'fc.fcHeader.dstId',
        'CS_CTL/Priority': 'fc.fcHeader.csCTLPriority',
        'Source ID': 'fc.fcHeader.srcId',
        'Type': 'fc.fcHeader.type',
        'F_CTL': 'fc.fcHeader.fCTL',
        'SEQ_ID': 'fc.fcHeader.seqID',
        'DF_CTL': 'fc.fcHeader.dfCTL',
        'SEQ_CNT': 'fc.fcHeader.seqCNT',
        'OX_ID': 'fc.fcHeader.oxID',
        'RX_ID': 'fc.fcHeader.rxID',
        'Parameter': 'fc.fcHeader.parameter',
    }

    def __init__(self, parent):
        super(FC, self).__init__(parent)

    @property
    def SOF(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SOF']))

    @property
    def R_CTL(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['R_CTL']))

    @property
    def Destination_ID(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Destination ID']))

    @property
    def CS_CTL_Priority(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CS_CTL/Priority']))

    @property
    def Source_ID(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Source ID']))

    @property
    def Type(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Type']))

    @property
    def F_CTL(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['F_CTL']))

    @property
    def SEQ_ID(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SEQ_ID']))

    @property
    def DF_CTL(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DF_CTL']))

    @property
    def SEQ_CNT(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SEQ_CNT']))

    @property
    def OX_ID(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['OX_ID']))

    @property
    def RX_ID(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RX_ID']))

    @property
    def Parameter(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Parameter']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
