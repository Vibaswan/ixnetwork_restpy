from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class FCoE_DIA_Request(Base):
    __slots__ = ()
    _SDM_NAME = 'fCoEDIARequest'
    _SDM_ATT_MAP = {
        'FCoE Header': 'fCoEDIARequest.header.fcoeHeader',
        'FC Header': 'fCoEDIARequest.header.fcHeader',
        'FC Command': 'fCoEDIARequest.header.fcCmd',
        'Reserved1': 'fCoEDIARequest.header.reserved1',
        'Originating Switch_Name': 'fCoEDIARequest.header.origSwitchName',
        'Reserved2': 'fCoEDIARequest.header.reserved2',
    }

    def __init__(self, parent):
        super(FCoE_DIA_Request, self).__init__(parent)

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
    def Originating_Switch_Name(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Originating Switch_Name']))

    @property
    def Reserved2(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Reserved2']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
