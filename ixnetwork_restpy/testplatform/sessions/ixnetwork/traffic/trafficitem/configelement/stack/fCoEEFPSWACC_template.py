from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class FCoE_EFP_SW_ACC(Base):
    __slots__ = ()
    _SDM_NAME = 'fCoEEFPSWACC'
    _SDM_ATT_MAP = {
        'FCoE Header': 'fCoEEFPSWACC.header.fcoeHeader',
        'FC Header': 'fCoEEFPSWACC.header.fcHeader',
        'FC Command': 'fCoEEFPSWACC.header.fcCmd',
        'Reserved1': 'fCoEEFPSWACC.header.reserved1',
        'Reserved2': 'fCoEEFPSWACC.header.reserved2',
        'Payload Length': 'fCoEEFPSWACC.header.length',
        'Reserved3': 'fCoEEFPSWACC.header.reserved3',
        'Principal Switch_Priority': 'fCoEEFPSWACC.header.principalSwitchPriority',
        'Principal Switch_Name': 'fCoEEFPSWACC.header.principalSwitchName',
        'Record_Type': 'fCoEEFPSWACC.header.recordType',
        'Domain_ID': 'fCoEEFPSWACC.header.domainID',
        'Reserved4': 'fCoEEFPSWACC.header.reserved4',
        'Reserved5': 'fCoEEFPSWACC.header.reserved5',
        'Switch_Name': 'fCoEEFPSWACC.header.switchName',
    }

    def __init__(self, parent):
        super(FCoE_EFP_SW_ACC, self).__init__(parent)

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
    def Principal_Switch_Priority(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Principal Switch_Priority']))

    @property
    def Principal_Switch_Name(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Principal Switch_Name']))

    @property
    def Record_Type(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Record_Type']))

    @property
    def Domain_ID(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Domain_ID']))

    @property
    def Reserved4(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Reserved4']))

    @property
    def Reserved5(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Reserved5']))

    @property
    def Switch_Name(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Switch_Name']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
