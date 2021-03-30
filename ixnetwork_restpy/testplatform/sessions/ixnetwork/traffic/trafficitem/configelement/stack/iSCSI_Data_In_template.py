from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class iSCSI_Data_In(Base):
    __slots__ = ()
    _SDM_NAME = 'iSCSI_Data_In'
    _SDM_ATT_MAP = {
        'Opcode': 'iSCSI_Data_In.header.Opcode',
        'Flags': 'iSCSI_Data_In.header.Flags',
        'TotalAHSLength': 'iSCSI_Data_In.header.TotalAHSLength',
        'Unknown': 'iSCSI_Data_In.header.Unknown',
        'DataSegmentLength': 'iSCSI_Data_In.header.DataSegmentLength',
        'LUN': 'iSCSI_Data_In.header.LUN',
        'InitiatorTaskTag': 'iSCSI_Data_In.header.InitiatorTaskTag',
        'TargetTransferTag': 'iSCSI_Data_In.header.TargetTransferTag',
        'StatSN': 'iSCSI_Data_In.header.StatSN',
        'ExpCmdSN': 'iSCSI_Data_In.header.ExpCmdSN',
        'MaxCmdSN': 'iSCSI_Data_In.header.MaxCmdSN',
        'DataSN': 'iSCSI_Data_In.header.DataSN',
        'Bufferoffset': 'iSCSI_Data_In.header.Bufferoffset',
        'ResidualCount': 'iSCSI_Data_In.header.ResidualCount',
        'HeaderDigest': 'iSCSI_Data_In.header.HeaderDigest',
    }

    def __init__(self, parent):
        super(iSCSI_Data_In, self).__init__(parent)

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
    def Unknown(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Unknown']))

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
    def StatSN(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['StatSN']))

    @property
    def ExpCmdSN(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ExpCmdSN']))

    @property
    def MaxCmdSN(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MaxCmdSN']))

    @property
    def DataSN(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DataSN']))

    @property
    def Bufferoffset(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Bufferoffset']))

    @property
    def ResidualCount(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ResidualCount']))

    @property
    def HeaderDigest(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['HeaderDigest']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
