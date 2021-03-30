from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class BMAC_Header(Base):
    __slots__ = ()
    _SDM_NAME = 'bMacHeader'
    _SDM_ATT_MAP = {
        'B-Destination Address (Ethernet)': 'bMacHeader.header.bDstAddress',
        'B-Source Address (Ethernet)': 'bMacHeader.header.bSrcAddress',
    }

    def __init__(self, parent):
        super(BMAC_Header, self).__init__(parent)

    @property
    def B_Destination_Address_Ethernet(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['B-Destination Address (Ethernet)']))

    @property
    def B_Source_Address_Ethernet(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['B-Source Address (Ethernet)']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
