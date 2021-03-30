from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class FCoE_RDI_SW_ACC(Base):
    __slots__ = ()
    _SDM_NAME = 'fCoERDISWACC'
    _SDM_ATT_MAP = {
        'FCoE Header': 'fCoERDISWACC.header.fcoeHeader',
        'FC Header': 'fCoERDISWACC.header.fcHeader',
        'FC Command': 'fCoERDISWACC.header.fcCmd',
        'Reserved1': 'fCoERDISWACC.header.reserved1',
        'Reserved2': 'fCoERDISWACC.header.reserved2',
        'Payload Length': 'fCoERDISWACC.header.length',
        'Reserved3': 'fCoERDISWACC.header.reserved3',
        'Granted Domain_ID': 'fCoERDISWACC.header.grantedDID',
    }

    def __init__(self, parent):
        super(FCoE_RDI_SW_ACC, self).__init__(parent)

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
    def Reserved3(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Reserved3']))

    @property
    def Granted_Domain_ID(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Granted Domain_ID']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
