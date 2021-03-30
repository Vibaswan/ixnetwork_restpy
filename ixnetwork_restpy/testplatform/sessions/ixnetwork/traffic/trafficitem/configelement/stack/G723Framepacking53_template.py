from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class G723_Frame_Packing_53(Base):
    __slots__ = ()
    _SDM_NAME = 'G723Framepacking5.3'
    _SDM_ATT_MAP = {
    }

    def __init__(self, parent):
        super(G723_Frame_Packing_53, self).__init__(parent)

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
