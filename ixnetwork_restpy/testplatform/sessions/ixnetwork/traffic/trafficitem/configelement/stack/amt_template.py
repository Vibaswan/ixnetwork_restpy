from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class AMT(Base):
    __slots__ = ()
    _SDM_NAME = 'amt'
    _SDM_ATT_MAP = {
        'Message Types': 'amt.header.messageTypes',
    }

    def __init__(self, parent):
        super(AMT, self).__init__(parent)

    @property
    def Message_Types(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Message Types']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
