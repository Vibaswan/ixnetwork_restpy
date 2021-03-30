from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class FCoE_RNN_ID(Base):
    __slots__ = ()
    _SDM_NAME = 'fCoERNNID'
    _SDM_ATT_MAP = {
        'FCoE Header': 'fCoERNNID.header.fcoeHeader',
        'FC Header': 'fCoERNNID.header.fcHeader',
        'FC_CT': 'fCoERNNID.header.fcCT',
        'dNS': 'fCoERNNID.header.dNS',
    }

    def __init__(self, parent):
        super(FCoE_RNN_ID, self).__init__(parent)

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

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
