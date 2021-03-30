from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class FCoE_DIA_SW_ACC(Base):
    __slots__ = ()
    _SDM_NAME = 'fCoEDIASWACC'
    _SDM_ATT_MAP = {
        'FCoE Header': 'fCoEDIASWACC.header.fcoeHeader',
        'FC Header': 'fCoEDIASWACC.header.fcHeader',
        'FC Command': 'fCoEDIASWACC.header.fcCmd',
        'Reserved1': 'fCoEDIASWACC.header.reserved1',
        'Responding Switch_Name': 'fCoEDIASWACC.header.respSwitchName',
        'Reserved2': 'fCoEDIASWACC.header.reserved2',
    }

    def __init__(self, parent):
        super(FCoE_DIA_SW_ACC, self).__init__(parent)

    @property
    def FCoE_Header(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FCoE Header']))

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
    def Responding_Switch_Name(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Responding Switch_Name']))

    @property
    def Reserved2(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Reserved2']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
