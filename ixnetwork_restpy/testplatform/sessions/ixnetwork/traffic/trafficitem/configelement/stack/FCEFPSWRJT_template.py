from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class FC_EFP_SW_RJT(Base):
    __slots__ = ()
    _SDM_NAME = 'FCEFPSWRJT'
    _SDM_ATT_MAP = {
        'FC Header': 'fcEFPSWRJT.header.fcHeader',
        'FC Command': 'fcEFPSWRJT.header.fcCmd',
        'Reserved1': 'fcEFPSWRJT.header.reserved1',
        'Reserved2': 'fcEFPSWRJT.header.reserved2',
        'Reason Code': 'fcEFPSWRJT.header.reasonCode',
        'Reason Code Explanation': 'fcEFPSWRJT.header.reasonExplain',
        'Vendor Specific': 'fcEFPSWRJT.header.vendor',
    }

    def __init__(self, parent):
        super(FC_EFP_SW_RJT, self).__init__(parent)

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
    def Reason_Code(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Reason Code']))

    @property
    def Reason_Code_Explanation(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Reason Code Explanation']))

    @property
    def Vendor_Specific(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Vendor Specific']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
