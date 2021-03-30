from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class iSCSI_Data_Out(Base):
    __slots__ = ()
    _SDM_NAME = 'iSCSI_Data_Out'
    _SDM_ATT_MAP = {
        'Opcode': 'iSCSI_Data_Out.header.Opcode',
        'Flags': 'iSCSI_Data_Out.header.Flags',
        'TotalAHSLength': 'iSCSI_Data_Out.header.TotalAHSLength',
        'Unknown ': 'iSCSI_Data_Out.header.Unknown ',
        'DataSegmentLength': 'iSCSI_Data_Out.header.DataSegmentLength',
        'LUN': 'iSCSI_Data_Out.header.LUN',
        'InitiatorTaskTag': 'iSCSI_Data_Out.header.InitiatorTaskTag',
        'TargetTransferTag': 'iSCSI_Data_Out.header.TargetTransferTag',
        'ExpStatSN': 'iSCSI_Data_Out.header.field0',
        'DataSN': 'iSCSI_Data_Out.header.DataSN',
        'BufferOffset': 'iSCSI_Data_Out.header.BufferOffset',
        'HeaderDigest': 'iSCSI_Data_Out.header.HeaderDigest',
    }

    def __init__(self, parent):
        super(iSCSI_Data_Out, self).__init__(parent)

    @property
    def Opcode(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Opcode']))

    @property
    def Flags(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Flags']))

    @property
    def TotalAHSLength(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TotalAHSLength']))

    @property
    def Unknown_(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Unknown ']))

    @property
    def DataSegmentLength(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DataSegmentLength']))

    @property
    def LUN(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LUN']))

    @property
    def InitiatorTaskTag(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['InitiatorTaskTag']))

    @property
    def TargetTransferTag(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TargetTransferTag']))

    @property
    def ExpStatSN(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ExpStatSN']))

    @property
    def DataSN(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DataSN']))

    @property
    def BufferOffset(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BufferOffset']))

    @property
    def HeaderDigest(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['HeaderDigest']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
