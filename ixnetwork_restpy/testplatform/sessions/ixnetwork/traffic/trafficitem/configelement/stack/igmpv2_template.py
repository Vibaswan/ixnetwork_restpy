from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class IGMPv2(Base):
    __slots__ = ()
    _SDM_NAME = 'igmpv2'
    _SDM_ATT_MAP = {
        'Type': 'igmpv2.header.type',
        'Maximum response time (units 1/10 second)': 'igmpv2.header.maximumResponseTimeunits110Second',
        'Checksum': 'igmpv2.header.checksum',
        'Group address': 'igmpv2.header.groupAddress',
    }

    def __init__(self, parent):
        super(IGMPv2, self).__init__(parent)

    @property
    def Type(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Type']))

    @property
    def Maximum_response_time_units_1_10_second(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Maximum response time (units 1/10 second)']))

    @property
    def Checksum(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Checksum']))

    @property
    def Group_address(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Group address']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class IGMPv2(Base):
    __slots__ = ()
    _SDM_NAME = 'igmpv2'
    _SDM_ATT_MAP = {
        'Type': 'igmpv2.header.type',
        'Maximum response time (units 1/10 second)': 'igmpv2.header.maximumResponseTimeunits110Second',
        'Checksum': 'igmpv2.header.checksum',
        'Group address': 'igmpv2.header.groupAddress',
    }

    def __init__(self, parent):
        super(IGMPv2, self).__init__(parent)

    @property
    def Type(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Type']))

    @property
    def Maximum_response_time_units_1_10_second(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Maximum response time (units 1/10 second)']))

    @property
    def Checksum(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Checksum']))

    @property
    def Group_address(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Group address']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
