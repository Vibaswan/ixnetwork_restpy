from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class FC_GFT_ID(Base):
    __slots__ = ()
    _SDM_NAME = 'FCGFTID'
    _SDM_ATT_MAP = {
        'FC Header': 'fCGFTID.header.fcHeader',
        'FC_CT': 'fCGFTID.header.fcCT',
        'dNS': 'fCGFTID.header.dNS',
        'FC CRC': 'fCGFTID.header.fcCRC',
        'FC Trailer': 'fCGFTID.header.fcTrailer',
    }

    def __init__(self, parent):
        super(FC_GFT_ID, self).__init__(parent)

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
