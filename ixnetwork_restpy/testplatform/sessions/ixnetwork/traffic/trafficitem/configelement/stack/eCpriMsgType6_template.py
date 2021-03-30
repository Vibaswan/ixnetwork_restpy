from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class eCPRI_Msg_Type_Remote_Reset6(Base):
    __slots__ = ()
    _SDM_NAME = 'eCpriMsgType6'
    _SDM_ATT_MAP = {
        'resetid': 'eCpriMsgType6.header.resetid',
        'resetop': 'eCpriMsgType6.header.resetop',
        'userdata': 'eCpriMsgType6.header.header',
    }

    def __init__(self, parent):
        super(eCPRI_Msg_Type_Remote_Reset6, self).__init__(parent)

    @property
    def resetid(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['resetid']))

    @property
    def resetop(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['resetop']))

    @property
    def userdata(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['userdata']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
