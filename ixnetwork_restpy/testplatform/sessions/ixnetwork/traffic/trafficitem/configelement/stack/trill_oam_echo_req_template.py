from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class TRILL_OAM_Echo_Request(Base):
    __slots__ = ()
    _SDM_NAME = 'trill_oam_echo_req'
    _SDM_ATT_MAP = {
        'SPID': 'trill_oam_echo_req.header.spid',
        'Sequence Number': 'trill_oam_echo_req.header.sequence',
    }

    def __init__(self, parent):
        super(TRILL_OAM_Echo_Request, self).__init__(parent)

    @property
    def SPID(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SPID']))

    @property
    def Sequence_Number(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Sequence Number']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
