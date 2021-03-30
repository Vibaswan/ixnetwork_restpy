from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class IGMPv3_Membership_Query(Base):
    __slots__ = ()
    _SDM_NAME = 'igmpv3MembershipQuery'
    _SDM_ATT_MAP = {
        'Type': 'igmpv3MembershipQuery.header.type',
        'Maximum response code (units 1/10 second)': 'igmpv3MembershipQuery.header.maximumResponseCodeunits110Second',
        'Checksum': 'igmpv3MembershipQuery.header.checksum',
        'Group address': 'igmpv3MembershipQuery.header.groupAddress',
        'Reserved': 'igmpv3MembershipQuery.header.reserved',
        'Suppress router-side processing (S-flag)': 'igmpv3MembershipQuery.header.suppressRoutersideProcessingSflag',
        'Queriers Robustness Variable': 'igmpv3MembershipQuery.header.qrv',
        'Queriers Query Interval Code': 'igmpv3MembershipQuery.header.qqic',
        'Number of sources': 'igmpv3MembershipQuery.header.numberOfSources',
        'Multicast sources': 'igmpv3MembershipQuery.header.multicastSources',
    }

    def __init__(self, parent):
        super(IGMPv3_Membership_Query, self).__init__(parent)

    @property
    def Type(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Type']))

    @property
    def Maximum_response_code_units_1_10_second(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Maximum response code (units 1/10 second)']))

    @property
    def Checksum(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Checksum']))

    @property
    def Group_address(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Group address']))

    @property
    def Reserved(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Reserved']))

    @property
    def Suppress_router_side_processing_S_flag(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Suppress router-side processing (S-flag)']))

    @property
    def Queriers_Robustness_Variable(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Queriers Robustness Variable']))

    @property
    def Queriers_Query_Interval_Code(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Queriers Query Interval Code']))

    @property
    def Number_of_sources(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Number of sources']))

    @property
    def Multicast_sources(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Multicast sources']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
