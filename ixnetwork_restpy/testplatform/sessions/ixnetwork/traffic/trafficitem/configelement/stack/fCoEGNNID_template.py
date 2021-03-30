from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class FCoE_GNN_ID(Base):
    __slots__ = ()
    _SDM_NAME = 'fCoEGNNID'
    _SDM_ATT_MAP = {
        'FCoE Header': 'fCoEGNNID.header.fcoeHeader',
        'FC Header': 'fCoEGNNID.header.fcHeader',
        'FC_CT': 'fCoEGNNID.header.fcCT',
        'dNS': 'fCoEGNNID.header.dNS',
        'FC CRC': 'fCoEGNNID.header.fcCRC',
        'FC Trailer': 'fCoEGNNID.header.fcTrailer',
    }

    def __init__(self, parent):
        super(FCoE_GNN_ID, self).__init__(parent)

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
