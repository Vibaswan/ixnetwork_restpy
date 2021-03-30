from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class NVGRE(Base):
    __slots__ = ()
    _SDM_NAME = 'nvgre'
    _SDM_ATT_MAP = {
        'Checksum Present': 'nvgre.header.checksumPresent',
        'Reserved': 'nvgre.header.reserved1',
        'Key Present': 'nvgre.header.keyPresent',
        'Sequence Number Present': 'nvgre.header.sequencePresent',
        'Reserved': 'nvgre.header.reserved2',
        'Version': 'nvgre.header.version',
        'Protocol': 'nvgre.header.protocol',
        'Checksum Option': 'nvgre.header.checksumHolder',
        'Virtual Subnet ID': 'nvgre.header.vsid',
        'Flow ID': 'nvgre.header.flowId',
        'Sequence Option': 'nvgre.header.sequenceHolder',
    }

    def __init__(self, parent):
        super(NVGRE, self).__init__(parent)

    @property
    def Checksum_Present(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Checksum Present']))

    @property
    def Reserved(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Reserved']))

    @property
    def Key_Present(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Key Present']))

    @property
    def Sequence_Number_Present(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Sequence Number Present']))

    @property
    def Reserved(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Reserved']))

    @property
    def Version(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Version']))

    @property
    def Protocol(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Protocol']))

    @property
    def Checksum_Option(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Checksum Option']))

    @property
    def Virtual_Subnet_ID(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Virtual Subnet ID']))

    @property
    def Flow_ID(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Flow ID']))

    @property
    def Sequence_Option(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Sequence Option']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
