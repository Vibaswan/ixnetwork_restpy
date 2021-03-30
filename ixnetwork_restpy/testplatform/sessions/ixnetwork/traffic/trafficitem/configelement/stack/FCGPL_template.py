from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class FC_GPL(Base):
    __slots__ = ()
    _SDM_NAME = 'FCGPL'
    _SDM_ATT_MAP = {
        'FC Header': 'fCGPL.header.fcHeader',
        'FC_CT': 'fCGPL.header.fcCT',
        'FCS': 'fCGPL.header.FCS',
        'FC CRC': 'fCGPL.header.fcCRC',
        'FC Trailer': 'fCGPL.header.fcTrailer',
    }

    def __init__(self, parent):
        super(FC_GPL, self).__init__(parent)

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
