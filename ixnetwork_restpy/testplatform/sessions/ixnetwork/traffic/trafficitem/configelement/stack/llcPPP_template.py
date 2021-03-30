from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class LLC_PPP(Base):
    __slots__ = ()
    _SDM_NAME = 'llcPPP'
    _SDM_ATT_MAP = {
        'Logical Link Control(LLC) Header': 'llcPPP.llcPPPHheader.llcHeader',
        'NLPID': 'llcPPP.llcPPPHheader.nlpid',
        'Protocol ID (PID)': 'llcPPP.llcPPPHheader.pid',
    }

    def __init__(self, parent):
        super(LLC_PPP, self).__init__(parent)

    @property
    def Logical_Link_ControlLLC_Header(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Logical Link Control(LLC) Header']))

    @property
    def NLPID(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['NLPID']))

    @property
    def Protocol_ID_PID(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Protocol ID (PID)']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
