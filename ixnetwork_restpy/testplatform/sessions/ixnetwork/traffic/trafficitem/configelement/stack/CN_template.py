from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class CN(Base):
    __slots__ = ()
    _SDM_NAME = 'CN'
    _SDM_ATT_MAP = {
        'Level Bit 1': 'CN.CNCommonHeader.levelbit1',
        'Level': 'CN.CNCommonHeader.level',
    }

    def __init__(self, parent):
        super(CN, self).__init__(parent)

    @property
    def Level_Bit_1(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Level Bit 1']))

    @property
    def Level(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Level']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
