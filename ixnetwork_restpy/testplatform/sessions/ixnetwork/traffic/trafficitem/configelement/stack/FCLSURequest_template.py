from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class FC_LSU_Request(Base):
    __slots__ = ()
    _SDM_NAME = 'FCLSURequest'
    _SDM_ATT_MAP = {
        'FC Header': 'fcLSURequest.header.fcHeader',
        'FC Command': 'fcLSURequest.header.fcCmd',
        'FSPF Header': 'fcLSURequest.header.fspfHeader',
        'Reserved': 'fcLSURequest.header.reserved',
        'Flags': 'fcLSURequest.header.flags',
        'Number of Link State Record Headers': 'fcLSURequest.header.nrLSRhs',
        'Link State Header': 'fcLSURequest.header.linkStateHeader',
    }

    def __init__(self, parent):
        super(FC_LSU_Request, self).__init__(parent)

    @property
    def FC_Header(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FC Header']))

    @property
    def FC_Command(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FC Command']))

    @property
    def FSPF_Header(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FSPF Header']))

    @property
    def Reserved(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Reserved']))

    @property
    def Flags(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Flags']))

    @property
    def Number_of_Link_State_Record_Headers(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Number of Link State Record Headers']))

    @property
    def Link_State_Header(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Link State Header']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
