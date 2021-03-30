from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class FCoE_RSNN_NN(Base):
    __slots__ = ()
    _SDM_NAME = 'fCoERSNNNN'
    _SDM_ATT_MAP = {
        'FCoE Header': 'fCoERSNNNN.header.fcoeHeader',
        'FC Header': 'fCoERSNNNN.header.fcHeader',
        'FC_CT': 'fCoERSNNNN.header.fcCT',
        'dNS': 'fCoERSNNNN.header.dNS',
        'FC CRC': 'fCoERSNNNN.header.fcCRC',
        'FC Trailer': 'fCoERSNNNN.header.fcTrailer',
    }

    def __init__(self, parent):
        super(FCoE_RSNN_NN, self).__init__(parent)

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
