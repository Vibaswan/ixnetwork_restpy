from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class INT_Metadata(Base):
    __slots__ = ()
    _SDM_NAME = 'intmetadata'
    _SDM_ATT_MAP = {
        'Version': 'intmetadata.intmetadata.version',
        'Replication': 'intmetadata.intmetadata.replication',
        'Copy': 'intmetadata.intmetadata.copy',
        'Max Hop Count Exceeded': 'intmetadata.intmetadata.exceeded',
        'MTU Exceeded': 'intmetadata.intmetadata.mtuexceeded',
        'Reserved': 'intmetadata.intmetadata.reserved10',
        'Hop Metadata Length (x4 bytes)': 'intmetadata.intmetadata.hopml',
        'Remaining Hop Count': 'intmetadata.intmetadata.remaininghopcount',
        'Instruction Bit Map': 'intmetadata.intmetadata.instbitmap',
        'Reserved': 'intmetadata.intmetadata.reserved16',
        'INT Metadata Stack': 'intmetadata.intmetadata.intmetadatastack',
    }

    def __init__(self, parent):
        super(INT_Metadata, self).__init__(parent)

    @property
    def Version(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Version']))

    @property
    def Replication(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Replication']))

    @property
    def Copy(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Copy']))

    @property
    def Max_Hop_Count_Exceeded(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Max Hop Count Exceeded']))

    @property
    def MTU_Exceeded(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MTU Exceeded']))

    @property
    def Reserved(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Reserved']))

    @property
    def Hop_Metadata_Length_x4_bytes(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Hop Metadata Length (x4 bytes)']))

    @property
    def Remaining_Hop_Count(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Remaining Hop Count']))

    @property
    def Instruction_Bit_Map(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Instruction Bit Map']))

    @property
    def Reserved(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Reserved']))

    @property
    def INT_Metadata_Stack(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['INT Metadata Stack']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
