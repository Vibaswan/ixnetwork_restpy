from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class FCoE_GPLI(Base):
    __slots__ = ()
    _SDM_NAME = 'fCoEGPLI'
    _SDM_ATT_MAP = {
        'FCoE Header': 'fCoEGPLI.header.fcoeHeader',
        'FC Header': 'fCoEGPLI.header.fcHeader',
        'FC_CT': 'fCoEGPLI.header.fcCT',
        'FCS': 'fCoEGPLI.header.FCS',
        'FC CRC': 'fCoEGPLI.header.fcCRC',
        'FC Trailer': 'fCoEGPLI.header.fcTrailer',
    }

    def __init__(self, parent):
        super(FCoE_GPLI, self).__init__(parent)

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
