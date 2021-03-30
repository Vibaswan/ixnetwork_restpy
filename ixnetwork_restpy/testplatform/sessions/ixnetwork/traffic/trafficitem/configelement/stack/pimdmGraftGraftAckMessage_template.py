from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class PIM_DM_Graft_Graft_Ack_Message(Base):
    __slots__ = ()
    _SDM_NAME = 'pimdmGraftGraftAckMessage'
    _SDM_ATT_MAP = {
    }

    def __init__(self, parent):
        super(PIM_DM_Graft_Graft_Ack_Message, self).__init__(parent)

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
