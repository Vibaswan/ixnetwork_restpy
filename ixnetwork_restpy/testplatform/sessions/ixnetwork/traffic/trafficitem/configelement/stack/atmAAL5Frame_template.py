from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Atm_Aal5_Frame(Base):
    __slots__ = ()
    _SDM_NAME = 'atmAAL5Frame'
    _SDM_ATT_MAP = {
        'LLC Header': 'atmAAL5Frame.header.llcHeader',
        'AAL5 OUI': 'atmAAL5Frame.header.aal5OUI',
        'Protocol Type': 'atmAAL5Frame.header.protocolType',
    }

    def __init__(self, parent):
        super(Atm_Aal5_Frame, self).__init__(parent)

    @property
    def LLC_Header(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LLC Header']))

    @property
    def AAL5_OUI(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AAL5 OUI']))

    @property
    def Protocol_Type(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Protocol Type']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
