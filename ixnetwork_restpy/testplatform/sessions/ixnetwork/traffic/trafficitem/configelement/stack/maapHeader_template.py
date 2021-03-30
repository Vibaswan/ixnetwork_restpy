from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class MAC_Address_Acquisition_Header(Base):
    __slots__ = ()
    _SDM_NAME = 'maapHeader'
    _SDM_ATT_MAP = {
    }

    def __init__(self, parent):
        super(MAC_Address_Acquisition_Header, self).__init__(parent)

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
