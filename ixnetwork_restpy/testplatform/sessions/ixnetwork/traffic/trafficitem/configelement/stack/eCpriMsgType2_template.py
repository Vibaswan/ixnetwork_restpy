from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class eCPRI_Msg_Type_Real_Time_Control_Data2(Base):
    __slots__ = ()
    _SDM_NAME = 'eCpriMsgType2'
    _SDM_ATT_MAP = {
        'rtcid': 'eCpriMsgType2.header.rtcid',
        'seqid': 'eCpriMsgType2.header.seqid',
        'userdata': 'eCpriMsgType2.header.header',
    }

    def __init__(self, parent):
        super(eCPRI_Msg_Type_Real_Time_Control_Data2, self).__init__(parent)

    @property
    def rtcid(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['rtcid']))

    @property
    def seqid(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['seqid']))

    @property
    def userdata(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['userdata']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
