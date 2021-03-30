from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class IEC_61883_6_24_Bit_Data(Base):
    __slots__ = ()
    _SDM_NAME = 'iec61883-6_24-BitData'
    _SDM_ATT_MAP = {
    }

    def __init__(self, parent):
        super(IEC_61883_6_24_Bit_Data, self).__init__(parent)

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
