from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class eCPRI_Msg_Type_One_way_Delay_Measurement5(Base):
    __slots__ = ()
    _SDM_NAME = 'eCpriMsgType5'
    _SDM_ATT_MAP = {
        'mid': 'eCpriMsgType5.header.mid',
        'atype': 'eCpriMsgType5.header.atype',
        'timestamp': 'eCpriMsgType5.header.timestamp',
        'compvalue': 'eCpriMsgType5.header.compvalue',
        'userdata': 'eCpriMsgType5.header.header',
    }

    def __init__(self, parent):
        super(eCPRI_Msg_Type_One_way_Delay_Measurement5, self).__init__(parent)

    @property
    def mid(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['mid']))

    @property
    def atype(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['atype']))

    @property
    def timestamp(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['timestamp']))

    @property
    def compvalue(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['compvalue']))

    @property
    def userdata(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['userdata']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
