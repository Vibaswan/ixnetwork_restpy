from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class FCoE_GFT_ID(Base):
    __slots__ = ()
    _SDM_NAME = 'fCoEGFTID'
    _SDM_ATT_MAP = {
        'FCoE Header': 'fCoEGFTID.header.fcoeHeader',
        'FC Header': 'fCoEGFTID.header.fcHeader',
        'FC_CT': 'fCoEGFTID.header.fcCT',
        'dNS': 'fCoEGFTID.header.dNS',
        'FC CRC': 'fCoEGFTID.header.fcCRC',
        'FC Trailer': 'fCoEGFTID.header.fcTrailer',
    }

    def __init__(self, parent):
        super(FCoE_GFT_ID, self).__init__(parent)

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
