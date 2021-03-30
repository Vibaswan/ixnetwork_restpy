from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class FC_ELP_Request(Base):
    __slots__ = ()
    _SDM_NAME = 'FCELPRequest'
    _SDM_ATT_MAP = {
        'FC Header': 'fcELPRequest.header.fcHeader',
        'FC Command': 'fcELPRequest.header.fcCmd',
        'Reserved1': 'fcELPRequest.header.reserved1',
        'Revision': 'fcELPRequest.header.revision',
        'Flags': 'fcELPRequest.header.flags',
        'BB_SC_N': 'fcELPRequest.header.bbScN',
        'R_A_TOV': 'fcELPRequest.header.rATov',
        'E_D_TOV': 'fcELPRequest.header.eDTov',
        'Requester Interconnect_Port_Name': 'fcELPRequest.header.reqInterconnectPortName',
        'Requester Switch_Name': 'fcELPRequest.header.reqSwitchName',
        'Fabric Controller Class F Service Parameters': 'fcELPRequest.header.serviceParams',
        'Class 1 Interconnect_Port Parameters': 'fcELPRequest.header.class1PortParams',
        'Class 2 Interconnect_Port Parameters': 'fcELPRequest.header.class2PortParams',
        'Class 3 Interconnect_Port Parameters': 'fcELPRequest.header.class3PortParams',
        'Reserved2': 'fcELPRequest.header.reserved2',
        'ISL Flow Control Mode': 'fcELPRequest.header.islFlowControlMode',
        'Flow Control Parameter Length': 'fcELPRequest.header.flowControlParamLength',
        'Flow Control Parameters': 'fcELPRequest.header.flowControlParams',
    }

    def __init__(self, parent):
        super(FC_ELP_Request, self).__init__(parent)

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
    def Revision(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Revision']))

    @property
    def Flags(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Flags']))

    @property
    def BB_SC_N(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BB_SC_N']))

    @property
    def R_A_TOV(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['R_A_TOV']))

    @property
    def E_D_TOV(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['E_D_TOV']))

    @property
    def Requester_Interconnect_Port_Name(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Requester Interconnect_Port_Name']))

    @property
    def Requester_Switch_Name(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Requester Switch_Name']))

    @property
    def Fabric_Controller_Class_F_Service_Parameters(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Fabric Controller Class F Service Parameters']))

    @property
    def Class_1_Interconnect_Port_Parameters(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Class 1 Interconnect_Port Parameters']))

    @property
    def Class_2_Interconnect_Port_Parameters(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Class 2 Interconnect_Port Parameters']))

    @property
    def Class_3_Interconnect_Port_Parameters(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Class 3 Interconnect_Port Parameters']))

    @property
    def Reserved2(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Reserved2']))

    @property
    def ISL_Flow_Control_Mode(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ISL Flow Control Mode']))

    @property
    def Flow_Control_Parameter_Length(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Flow Control Parameter Length']))

    @property
    def Flow_Control_Parameters(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Flow Control Parameters']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
