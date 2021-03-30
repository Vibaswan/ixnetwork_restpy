from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class FC_RDI_SW_ACC(Base):
    __slots__ = ()
    _SDM_NAME = 'FCRDISWACC'
    _SDM_ATT_MAP = {
        'FC Header': 'fcRDISWACC.header.fcHeader',
        'FC Command': 'fcRDISWACC.header.fcCmd',
        'Reserved1': 'fcRDISWACC.header.reserved1',
        'Reserved2': 'fcRDISWACC.header.reserved2',
        'Payload Length': 'fcRDISWACC.header.length',
        'Reserved3': 'fcRDISWACC.header.reserved3',
        'Granted Domain_ID': 'fcRDISWACC.header.grantedDID',
    }

    def __init__(self, parent):
        super(FC_RDI_SW_ACC, self).__init__(parent)

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
