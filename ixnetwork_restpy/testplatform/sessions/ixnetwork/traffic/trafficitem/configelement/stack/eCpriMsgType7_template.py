from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class eCPRI_Msg_Type_Event_Indication7(Base):
    __slots__ = ()
    _SDM_NAME = 'eCpriMsgType7'
    _SDM_ATT_MAP = {
        'eventid': 'eCpriMsgType7.header.eventid',
        'eventtype': 'eCpriMsgType7.header.eventtype',
        'seqnum': 'eCpriMsgType7.header.seqnum',
        'faults': 'eCpriMsgType7.header.faults',
    }

    def __init__(self, parent):
        super(eCPRI_Msg_Type_Event_Indication7, self).__init__(parent)

    @property
    def eventid(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['eventid']))

    @property
    def eventtype(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['eventtype']))

    @property
    def seqnum(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['seqnum']))

    @property
    def faults(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['faults']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
