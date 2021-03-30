from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class FCoE_GPN_FT(Base):
    __slots__ = ()
    _SDM_NAME = 'fCoEGPNFT'
    _SDM_ATT_MAP = {
        'FCoE Header': 'fCoEGPNFT.header.fcoeHeader',
        'FC Header': 'fCoEGPNFT.header.fcHeader',
        'FC_CT': 'fCoEGPNFT.header.fcCT',
        'dNS': 'fCoEGPNFT.header.dNS',
        'FC CRC': 'fCoEGPNFT.header.fcCRC',
        'FC Trailer': 'fCoEGPNFT.header.fcTrailer',
    }

    def __init__(self, parent):
        super(FCoE_GPN_FT, self).__init__(parent)

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
