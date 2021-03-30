from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class IEC_61883_1(Base):
    __slots__ = ()
    _SDM_NAME = 'iec61883-1'
    _SDM_ATT_MAP = {
        'CIP 1': 'iec61883-1.header.CIP-1',
        'CIP 2': 'iec61883-1.header.CIP-2',
        'Select FDF': 'iec61883-1.header.selectFDF',
    }

    def __init__(self, parent):
        super(IEC_61883_1, self).__init__(parent)

    @property
    def CIP_1(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CIP 1']))

    @property
    def CIP_2(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CIP 2']))

    @property
    def Select_FDF(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Select FDF']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
