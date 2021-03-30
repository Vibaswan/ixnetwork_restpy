from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class FCoE_LSU_Request(Base):
    __slots__ = ()
    _SDM_NAME = 'fCoELSURequest'
    _SDM_ATT_MAP = {
        'FCoE Header': 'fCoELSURequest.header.fcoeHeader',
        'FC Header': 'fCoELSURequest.header.fcHeader',
        'FC Command': 'fCoELSURequest.header.fcCmd',
        'FSPF Header': 'fCoELSURequest.header.fspfHeader',
        'Reserved': 'fCoELSURequest.header.reserved',
        'Flags': 'fCoELSURequest.header.flags',
        'Number of Link State Record Headers': 'fCoELSURequest.header.nrLSRhs',
        'Link State Header': 'fCoELSURequest.header.linkStateHeader',
    }

    def __init__(self, parent):
        super(FCoE_LSU_Request, self).__init__(parent)

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
