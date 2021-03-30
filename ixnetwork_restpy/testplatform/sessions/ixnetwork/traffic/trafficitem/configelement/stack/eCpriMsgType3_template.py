from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class eCPRI_Msg_Type_Generic_Data_Transfer3(Base):
    __slots__ = ()
    _SDM_NAME = 'eCpriMsgType3'
    _SDM_ATT_MAP = {
        'pcid': 'eCpriMsgType3.header.pcid',
        'seqid': 'eCpriMsgType3.header.seqid',
        'userdata': 'eCpriMsgType3.header.header',
    }

    def __init__(self, parent):
        super(eCPRI_Msg_Type_Generic_Data_Transfer3, self).__init__(parent)

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
