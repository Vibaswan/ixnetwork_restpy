from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class PIM_Assert_Message(Base):
    __slots__ = ()
    _SDM_NAME = 'pimAssert'
    _SDM_ATT_MAP = {
        'Version': 'pimAssertMessage.header.version',
        'Type': 'pimAssertMessage.header.type',
        'Reserved': 'pimAssertMessage.header.reserved',
        'Checksum': 'pimAssertMessage.header.checksum',
        'Group Address': 'pimAssertMessage.header.groupAddress',
        'Source Address': 'pimAssertMessage.header.sourceAddress',
        'R ': 'pimAssertMessage.header.r',
        'Metric Preference ': 'pimAssertMessage.header.metricPreference',
        'Metric ': 'pimAssertMessage.header.metric',
    }

    def __init__(self, parent):
        super(PIM_Assert_Message, self).__init__(parent)

    @property
    def Version(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Version']))

    @property
    def Type(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Type']))

    @property
    def Reserved(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Reserved']))

    @property
    def Checksum(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Checksum']))

    @property
    def Group_Address(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Group Address']))

    @property
    def Source_Address(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Source Address']))

    @property
    def R_(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['R ']))

    @property
    def Metric_Preference_(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Metric Preference ']))

    @property
    def Metric_(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Metric ']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
