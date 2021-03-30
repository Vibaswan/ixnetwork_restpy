from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class PFC_PAUSE_8021Qbb(Base):
    __slots__ = ()
    _SDM_NAME = 'pfcPause'
    _SDM_ATT_MAP = {
        'Ethernet Header': 'pfcPause.header.header',
        'MAC Control': 'pfcPause.header.macControl',
    }

    def __init__(self, parent):
        super(PFC_PAUSE_8021Qbb, self).__init__(parent)

    @property
    def Ethernet_Header(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Ethernet Header']))

    @property
    def MAC_Control(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MAC Control']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
