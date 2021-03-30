from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class eCPRI_Msg_Type_IQ_Data0(Base):
    __slots__ = ()
    _SDM_NAME = 'eCpriMsgType0'
    _SDM_ATT_MAP = {
        'pcid': 'eCpriMsgType0.header.pcid',
        'seqid': 'eCpriMsgType0.header.seqid',
        'userdata': 'eCpriMsgType0.header.header',
    }

    def __init__(self, parent):
        super(eCPRI_Msg_Type_IQ_Data0, self).__init__(parent)

    @property
    def pcid(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['pcid']))

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
