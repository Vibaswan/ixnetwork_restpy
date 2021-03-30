from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class FCoE_GSNN_NN(Base):
    __slots__ = ()
    _SDM_NAME = 'fCoEGSNNNN'
    _SDM_ATT_MAP = {
        'FCoE Header': 'fCoEGSNNNN.header.fcoeHeader',
        'FC Header': 'fCoEGSNNNN.header.fcHeader',
        'FC_CT': 'fCoEGSNNNN.header.fcCT',
        'dNS': 'fCoEGSNNNN.header.dNS',
        'FC CRC': 'fCoEGSNNNN.header.fcCRC',
        'FC Trailer': 'fCoEGSNNNN.header.fcTrailer',
    }

    def __init__(self, parent):
        super(FCoE_GSNN_NN, self).__init__(parent)

    @property
    def FCoE_Header(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FCoE Header']))

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
