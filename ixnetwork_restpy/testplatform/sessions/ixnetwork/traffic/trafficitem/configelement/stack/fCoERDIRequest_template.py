from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class FCoE_RDI_Request(Base):
    __slots__ = ()
    _SDM_NAME = 'fCoERDIRequest'
    _SDM_ATT_MAP = {
        'FCoE Header': 'fCoERDIRequest.header.fcoeHeader',
        'FC Header': 'fCoERDIRequest.header.fcHeader',
        'FC Command': 'fCoERDIRequest.header.fcCmd',
        'Reserved1': 'fCoERDIRequest.header.reserved1',
        'Reserved2': 'fCoERDIRequest.header.reserved2',
        'Payload Length': 'fCoERDIRequest.header.length',
        'Requesting Switch_Name': 'fCoERDIRequest.header.reqSwitchName',
        'Reserved3': 'fCoERDIRequest.header.reserved3',
        'Requested Domain_ID': 'fCoERDIRequest.header.reqDID',
    }

    def __init__(self, parent):
        super(FCoE_RDI_Request, self).__init__(parent)

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
    def Reserved2(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Reserved2']))

    @property
    def Payload_Length(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Payload Length']))

    @property
    def Requesting_Switch_Name(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Requesting Switch_Name']))

    @property
    def Reserved3(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Reserved3']))

    @property
    def Requested_Domain_ID(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Requested Domain_ID']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
