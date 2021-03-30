from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class FCoE_MR_SW_RJT(Base):
    __slots__ = ()
    _SDM_NAME = 'fCoEMRSWRJT'
    _SDM_ATT_MAP = {
        'FCoE Header': 'fCoEMRSWRJT.header.fcoeHeader',
        'FC Header': 'fCoEMRSWRJT.header.fcHeader',
        'FC Command': 'fCoEMRSWRJT.header.fcCmd',
        'Reserved1': 'fCoEMRSWRJT.header.reserved1',
        'Reserved2': 'fCoEMRSWRJT.header.reserved2',
        'Reason Code': 'fCoEMRSWRJT.header.reasonCode',
        'Reason Code Explanation': 'fCoEMRSWRJT.header.reasonExplain',
        'Vendor Specific': 'fCoEMRSWRJT.header.vendor',
    }

    def __init__(self, parent):
        super(FCoE_MR_SW_RJT, self).__init__(parent)

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
