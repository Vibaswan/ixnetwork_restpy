from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class PPP_PAP_CHAP(Base):
    __slots__ = ()
    _SDM_NAME = 'pppPAPCHAP'
    _SDM_ATT_MAP = {
        'Authetication Protocol': 'pppPAPCHAP.header.authenticationProtocol',
    }

    def __init__(self, parent):
        super(PPP_PAP_CHAP, self).__init__(parent)

    @property
    def Authetication_Protocol(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Authetication Protocol']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
