from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class MSDP(Base):
    __slots__ = ()
    _SDM_NAME = 'msdp'
    _SDM_ATT_MAP = {
        'MSDP Messege Type': 'msdp.msdpMessage.msdpMessegeType',
    }

    def __init__(self, parent):
        super(MSDP, self).__init__(parent)

    @property
    def MSDP_Messege_Type(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MSDP Messege Type']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
