from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class G723_Sid_Mode(Base):
    __slots__ = ()
    _SDM_NAME = 'G723SidMode'
    _SDM_ATT_MAP = {
    }

    def __init__(self, parent):
        super(G723_Sid_Mode, self).__init__(parent)

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
