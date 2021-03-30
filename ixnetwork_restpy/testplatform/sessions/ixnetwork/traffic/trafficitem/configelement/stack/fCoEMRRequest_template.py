from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class FCoE_MR_Request(Base):
    __slots__ = ()
    _SDM_NAME = 'fCoEMRRequest'
    _SDM_ATT_MAP = {
        'FCoE Header': 'fCoEMRRequest.header.fcoeHeader',
        'FC Header': 'fCoEMRRequest.header.fcHeader',
        'FC Command': 'fCoEMRRequest.header.fcCmd',
        'Reserved1': 'fCoEMRRequest.header.reserved1',
        'Protocol Version': 'fCoEMRRequest.header.version',
        'Payload': 'fCoEMRRequest.header.length',
    }

    def __init__(self, parent):
        super(FCoE_MR_Request, self).__init__(parent)

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
    def Protocol_Version(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Protocol Version']))

    @property
    def Payload(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Payload']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
