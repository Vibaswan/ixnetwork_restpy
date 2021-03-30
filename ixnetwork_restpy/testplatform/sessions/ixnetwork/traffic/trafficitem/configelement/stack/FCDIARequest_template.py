from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class FC_DIA_Request(Base):
    __slots__ = ()
    _SDM_NAME = 'FCDIARequest'
    _SDM_ATT_MAP = {
        'FC Header': 'fcDIARequest.header.fcHeader',
        'FC Command': 'fcDIARequest.header.fcCmd',
        'Reserved1': 'fcDIARequest.header.reserved1',
        'Originating Switch_Name': 'fcDIARequest.header.origSwitchName',
        'Reserved2': 'fcDIARequest.header.reserved2',
    }

    def __init__(self, parent):
        super(FC_DIA_Request, self).__init__(parent)

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
