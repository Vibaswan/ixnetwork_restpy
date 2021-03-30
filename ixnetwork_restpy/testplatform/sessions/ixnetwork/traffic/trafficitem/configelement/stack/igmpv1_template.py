from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class IGMPv1(Base):
    __slots__ = ()
    _SDM_NAME = 'igmpv1'
    _SDM_ATT_MAP = {
        'Version': 'igmpv1.header.version',
        'Type': 'igmpv1.header.type',
        'Unused': 'igmpv1.header.unused',
        'Checksum': 'igmpv1.header.checksum',
        'Group address': 'igmpv1.header.groupAddress',
    }

    def __init__(self, parent):
        super(IGMPv1, self).__init__(parent)

    @property
    def Version(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Version']))

    @property
    def Type(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Type']))

    @property
    def Unused(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Unused']))

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


class IGMPv1(Base):
    __slots__ = ()
    _SDM_NAME = 'igmpv1'
    _SDM_ATT_MAP = {
        'Version': 'igmpv1.header.version',
        'Type': 'igmpv1.header.type',
        'Unused': 'igmpv1.header.unused',
        'Checksum': 'igmpv1.header.checksum',
        'Group address': 'igmpv1.header.groupAddress',
    }

    def __init__(self, parent):
        super(IGMPv1, self).__init__(parent)

    @property
    def Version(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Version']))

    @property
    def Type(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Type']))

    @property
    def Unused(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Unused']))

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
