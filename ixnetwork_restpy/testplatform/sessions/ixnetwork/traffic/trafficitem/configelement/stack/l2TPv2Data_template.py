from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class L2TPv2_Data_Message(Base):
    __slots__ = ()
    _SDM_NAME = 'l2TPv2Data'
    _SDM_ATT_MAP = {
    }

    def __init__(self, parent):
        super(L2TPv2_Data_Message, self).__init__(parent)

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
