from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class PPP(Base):
    __slots__ = ()
    _SDM_NAME = 'ppp'
    _SDM_ATT_MAP = {
        'PPP Address': 'ppp.header.address',
        'PPP Control': 'ppp.header.control',
        'PPP Protocol Type': 'ppp.header.protocolType',
    }

    def __init__(self, parent):
        super(PPP, self).__init__(parent)

    @property
    def PPP_Address(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PPP Address']))

    @property
    def PPP_Control(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PPP Control']))

    @property
    def PPP_Protocol_Type(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PPP Protocol Type']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
