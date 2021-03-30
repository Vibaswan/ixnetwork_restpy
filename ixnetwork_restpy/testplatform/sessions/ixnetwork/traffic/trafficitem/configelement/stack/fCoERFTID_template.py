from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class FCoE_RFT_ID(Base):
    __slots__ = ()
    _SDM_NAME = 'fCoERFTID'
    _SDM_ATT_MAP = {
        'FCoE Header': 'fCoERFTID.header.fcoeHeader',
        'FC Header': 'fCoERFTID.header.fcHeader',
        'FC_CT': 'fCoERFTID.header.fcCT',
        'dNS': 'fCoERFTID.header.dNS',
        'FC CRC': 'fCoERFTID.header.fcCRC',
        'FC Trailer': 'fCoERFTID.header.fcTrailer',
    }

    def __init__(self, parent):
        super(FCoE_RFT_ID, self).__init__(parent)

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
