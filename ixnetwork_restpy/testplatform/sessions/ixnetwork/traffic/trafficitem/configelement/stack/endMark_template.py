from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class MRP_End_Mark(Base):
    __slots__ = ()
    _SDM_NAME = 'endMark'
    _SDM_ATT_MAP = {
        'End Mark': 'endMark.header.endMark',
    }

    def __init__(self, parent):
        super(MRP_End_Mark, self).__init__(parent)

    @property
    def End_Mark(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['End Mark']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
