from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class FC_GSNN_NN(Base):
    __slots__ = ()
    _SDM_NAME = 'FCGSNNNN'
    _SDM_ATT_MAP = {
        'FC Header': 'fCGSNNNN.header.fcHeader',
        'FC_CT': 'fCGSNNNN.header.fcCT',
        'dNS': 'fCGSNNNN.header.dNS',
        'FC CRC': 'fCGSNNNN.header.fcCRC',
        'FC Trailer': 'fCGSNNNN.header.fcTrailer',
    }

    def __init__(self, parent):
        super(FC_GSNN_NN, self).__init__(parent)

    @property
    def FC_Header(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FC Header']))

    @property
    def FC_CT(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FC_CT']))

    @property
    def dNS(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['dNS']))

    @property
    def FC_CRC(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FC CRC']))

    @property
    def FC_Trailer(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FC Trailer']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
