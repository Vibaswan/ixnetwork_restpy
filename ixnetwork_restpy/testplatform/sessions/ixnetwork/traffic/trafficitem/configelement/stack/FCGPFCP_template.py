from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class FC_GPFCP(Base):
    __slots__ = ()
    _SDM_NAME = 'FCGPFCP'
    _SDM_ATT_MAP = {
        'FC Header': 'fCGPFCP.header.fcHeader',
        'FC_CT': 'fCGPFCP.header.fcCT',
        'FCS': 'fCGPFCP.header.FCS',
        'FC CRC': 'fCGPFCP.header.fcCRC',
        'FC Trailer': 'fCGPFCP.header.fcTrailer',
    }

    def __init__(self, parent):
        super(FC_GPFCP, self).__init__(parent)

    @property
    def FC_Header(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FC Header']))

    @property
    def FC_CT(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FC_CT']))

    @property
    def FCS(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FCS']))

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
