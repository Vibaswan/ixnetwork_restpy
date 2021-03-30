from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class FCoE_RPLT(Base):
    __slots__ = ()
    _SDM_NAME = 'fCoERPLT'
    _SDM_ATT_MAP = {
        'FCoE Header': 'fCoERPLT.header.fcoeHeader',
        'FC Header': 'fCoERPLT.header.fcHeader',
        'FC_CT': 'fCoERPLT.header.fcCT',
        'FCS': 'fCoERPLT.header.FCS',
        'FC CRC': 'fCoERPLT.header.fcCRC',
        'FC Trailer': 'fCoERPLT.header.fcTrailer',
    }

    def __init__(self, parent):
        super(FCoE_RPLT, self).__init__(parent)

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
