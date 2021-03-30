from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class L2TPv3_Data_Message_Over_IP(Base):
    __slots__ = ()
    _SDM_NAME = 'l2TPv3DataIP'
    _SDM_ATT_MAP = {
        'L2TP Session Header': 'l2TPv3DataIP.dataHeader.sessionHeader',
        'L2-Specific Sublayer': 'l2TPv3DataIP.dataHeader.l2Sublayer',
    }

    def __init__(self, parent):
        super(L2TPv3_Data_Message_Over_IP, self).__init__(parent)

    @property
    def L2TP_Session_Header(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['L2TP Session Header']))

    @property
    def L2_Specific_Sublayer(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['L2-Specific Sublayer']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
