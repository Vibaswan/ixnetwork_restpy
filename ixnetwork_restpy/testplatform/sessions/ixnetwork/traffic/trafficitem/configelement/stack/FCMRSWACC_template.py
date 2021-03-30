from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class FC_MR_SW_ACC(Base):
    __slots__ = ()
    _SDM_NAME = 'FCMRSWACC'
    _SDM_ATT_MAP = {
        'FC Header': 'fcMRSWACC.header.fcHeader',
        'FC Command': 'fcMRSWACC.header.fcCmd',
        'Reserved1': 'fcMRSWACC.header.reserved1',
        'Reserved2': 'fcMRSWACC.header.reserved2',
    }

    def __init__(self, parent):
        super(FC_MR_SW_ACC, self).__init__(parent)

    @property
    def FC_Header(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FC Header']))

    @property
    def FC_Command(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FC Command']))

    @property
    def Reserved1(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Reserved1']))

    @property
    def Reserved2(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Reserved2']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
