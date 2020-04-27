# MIT LICENSE
#
# Copyright 1997 - 2019 by IXIA Keysight
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE. 
from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class CMacProperties(Base):
    """BGP C-MAC Properties
    The CMacProperties class encapsulates a list of cMacProperties resources that are managed by the user.
    A list of resources can be retrieved from the server using the CMacProperties.find() method.
    The list can be managed by using the CMacProperties.add() and CMacProperties.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'cMacProperties'

    def __init__(self, parent):
        super(CMacProperties, self).__init__(parent)

    @property
    def BgpAsPathSegmentList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpaspathsegmentlist.BgpAsPathSegmentList): An instance of the BgpAsPathSegmentList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpaspathsegmentlist import BgpAsPathSegmentList
        return BgpAsPathSegmentList(self)

    @property
    def BgpClusterIdList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpclusteridlist.BgpClusterIdList): An instance of the BgpClusterIdList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpclusteridlist import BgpClusterIdList
        return BgpClusterIdList(self)

    @property
    def BgpCommunitiesList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpcommunitieslist.BgpCommunitiesList): An instance of the BgpCommunitiesList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpcommunitieslist import BgpCommunitiesList
        return BgpCommunitiesList(self)

    @property
    def BgpExtendedCommunitiesList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpextendedcommunitieslist.BgpExtendedCommunitiesList): An instance of the BgpExtendedCommunitiesList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpextendedcommunitieslist import BgpExtendedCommunitiesList
        return BgpExtendedCommunitiesList(self)

    @property
    def CMacProperties(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.cmacproperties.CMacProperties): An instance of the CMacProperties class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.cmacproperties import CMacProperties
        return CMacProperties(self)

    @property
    def EvpnIPv4PrefixRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.evpnipv4prefixrange.EvpnIPv4PrefixRange): An instance of the EvpnIPv4PrefixRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.evpnipv4prefixrange import EvpnIPv4PrefixRange
        return EvpnIPv4PrefixRange(self)

    @property
    def EvpnIPv6PrefixRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.evpnipv6prefixrange.EvpnIPv6PrefixRange): An instance of the EvpnIPv6PrefixRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.evpnipv6prefixrange import EvpnIPv6PrefixRange
        return EvpnIPv6PrefixRange(self)

    @property
    def Active(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Activate/Deactivate Configuration
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('active'))

    @property
    def ActiveTs(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Active TS
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('activeTs'))

    @property
    def AdvSrv6L2SidInIgp(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Advertise SRv6 L2 SID in IGP
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('advSrv6L2SidInIgp'))

    @property
    def AdvSrv6L3SidInIgp(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Advertise SRv6 L3 SID in IGP
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('advSrv6L3SidInIgp'))

    @property
    def AdvertiseIpv4Address(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Advertise IPv4 Address
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('advertiseIpv4Address'))

    @property
    def AdvertiseIpv6Address(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Advertise IPv6 Address
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('advertiseIpv6Address'))

    @property
    def AdvertiseSRv6L2SID(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Advertise SRv6 SID
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('advertiseSRv6L2SID'))

    @property
    def AdvertiseSRv6L3SID(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable SRv6 L3 SID
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('advertiseSRv6L3SID'))

    @property
    def AggregatorAs(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Aggregator AS
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('aggregatorAs'))

    @property
    def AggregatorId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Aggregator ID
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('aggregatorId'))

    @property
    def AsSetMode(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): AS# Set Mode
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('asSetMode'))

    @property
    def Count(self):
        """
        Returns
        -------
        - number: Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        """
        return self._get_attribute('count')

    @property
    def DescriptiveName(self):
        """
        Returns
        -------
        - str: Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offers more context
        """
        return self._get_attribute('descriptiveName')

    @property
    def EnableAggregatorId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Aggregator ID
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('enableAggregatorId'))

    @property
    def EnableAsPathSegments(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable AS Path Segments
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('enableAsPathSegments'))

    @property
    def EnableAtomicAggregate(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Atomic Aggregate
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('enableAtomicAggregate'))

    @property
    def EnableCluster(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Cluster
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('enableCluster'))

    @property
    def EnableCommunity(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Community
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('enableCommunity'))

    @property
    def EnableExtendedCommunity(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Extended Community
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('enableExtendedCommunity'))

    @property
    def EnableLocalPreference(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Local Preference
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('enableLocalPreference'))

    @property
    def EnableMultiExitDiscriminator(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Multi Exit
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('enableMultiExitDiscriminator'))

    @property
    def EnableNextHop(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Next Hop
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('enableNextHop'))

    @property
    def EnableOrigin(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Origin
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('enableOrigin'))

    @property
    def EnableOriginatorId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Originator ID
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('enableOriginatorId'))

    @property
    def EnableSecondLabel(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Second Label (L3)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('enableSecondLabel'))

    @property
    def EnableStickyStaticFlag(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Sticky/Static Flag
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('enableStickyStaticFlag'))

    @property
    def EnableUserDefinedSequenceNumber(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable User Defined Sequence Number
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('enableUserDefinedSequenceNumber'))

    @property
    def EviId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): EVI ID
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('eviId'))

    @property
    def FirstLabelStart(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): First Label (L2) Start
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('firstLabelStart'))

    @property
    def IncludeDefaultGatewayExtendedCommunity(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Include Default Gateway Extended Community
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('includeDefaultGatewayExtendedCommunity'))

    @property
    def Ipv4AddressPrefixLength(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IPv4 Address Prefix Length which is used to determine the intersubnetting between local and remote host
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('ipv4AddressPrefixLength'))

    @property
    def Ipv4NextHop(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IPv4 Next Hop
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('ipv4NextHop'))

    @property
    def Ipv6AddressPrefixLength(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IPv6 Address Prefix Length which is used to determine the intersubnetting between local and remote host
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('ipv6AddressPrefixLength'))

    @property
    def Ipv6NextHop(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IPv6 Next Hop
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('ipv6NextHop'))

    @property
    def LabelMode(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Label Mode
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('labelMode'))

    @property
    def LabelStep(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Label Step
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('labelStep'))

    @property
    def LocalPreference(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Local Preference
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('localPreference'))

    @property
    def Mac(self):
        """
        Returns
        -------
        - list(str): MAC addresses of the devices
        """
        return self._get_attribute('mac')

    @property
    def MultiExitDiscriminator(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Multi Exit
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('multiExitDiscriminator'))

    @property
    def Name(self):
        """
        Returns
        -------
        - str: Name of NGPF element, guaranteed to be unique in Scenario
        """
        return self._get_attribute('name')
    @Name.setter
    def Name(self, value):
        self._set_attribute('name', value)

    @property
    def NoOfASPathSegmentsPerRouteRange(self):
        """
        Returns
        -------
        - number: Number Of AS Path Segments Per Route Range
        """
        return self._get_attribute('noOfASPathSegmentsPerRouteRange')
    @NoOfASPathSegmentsPerRouteRange.setter
    def NoOfASPathSegmentsPerRouteRange(self, value):
        self._set_attribute('noOfASPathSegmentsPerRouteRange', value)

    @property
    def NoOfClusters(self):
        """
        Returns
        -------
        - number: Number of Clusters
        """
        return self._get_attribute('noOfClusters')
    @NoOfClusters.setter
    def NoOfClusters(self, value):
        self._set_attribute('noOfClusters', value)

    @property
    def NoOfCommunities(self):
        """
        Returns
        -------
        - number: Number of Communities
        """
        return self._get_attribute('noOfCommunities')
    @NoOfCommunities.setter
    def NoOfCommunities(self, value):
        self._set_attribute('noOfCommunities', value)

    @property
    def NoOfExtendedCommunity(self):
        """
        Returns
        -------
        - number: Number of Extended Communities
        """
        return self._get_attribute('noOfExtendedCommunity')
    @NoOfExtendedCommunity.setter
    def NoOfExtendedCommunity(self, value):
        self._set_attribute('noOfExtendedCommunity', value)

    @property
    def Origin(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Origin
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('origin'))

    @property
    def OriginatorId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Originator ID
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('originatorId'))

    @property
    def OverridePeerAsSetMode(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Override Peer AS# Set Mode
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('overridePeerAsSetMode'))

    @property
    def PeerAddress(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Peer IP Address
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('peerAddress'))

    @property
    def SecondLabelStart(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Second Label (L3) Start
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('secondLabelStart'))

    @property
    def SendSRv6SIDOptionalInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If we need to advertise SRv6 L2 SID Optional Information (Service Information sub-TLV) which is specified in next column(s)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('sendSRv6SIDOptionalInfo'))

    @property
    def SequenceNumber(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Sequence Number
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('sequenceNumber'))

    @property
    def SetNextHop(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Set Next Hop
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('setNextHop'))

    @property
    def SetNextHopIpType(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Set Next Hop IP Type
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('setNextHopIpType'))

    @property
    def Srv6EndpointBehavior(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SRv6 L2 Endpoint Behavior field Value for all routes in this Route Range
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('srv6EndpointBehavior'))

    @property
    def Srv6L2SidFlags(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SRv6 L2 SID Flags Value
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('srv6L2SidFlags'))

    @property
    def Srv6L2SidLoc(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SRv6 L2 SID. It consists of Locator, Func and Args
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('srv6L2SidLoc'))

    @property
    def Srv6L2SidLocLen(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SRv6 L2 SID Locator Length
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('srv6L2SidLocLen'))

    @property
    def Srv6L2SidLocMetric(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SRv6 L2 SID Locator Metric
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('srv6L2SidLocMetric'))

    @property
    def Srv6L2SidReserved(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SRv6 L2 SID Reserved Value (SRv6 SID Service TLV Level)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('srv6L2SidReserved'))

    @property
    def Srv6L2SidStep(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Route Range SRv6 SID Step
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('srv6L2SidStep'))

    @property
    def Srv6L3SidFlags(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SRv6 L3 SID Flags Value
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('srv6L3SidFlags'))

    @property
    def Srv6L3SidLoc(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SRv6 L3 SID. It consists of Locator, Func and Args
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('srv6L3SidLoc'))

    @property
    def Srv6L3SidLocLen(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SRv6 L3 SID Locator Length
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('srv6L3SidLocLen'))

    @property
    def Srv6L3SidLocMetric(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SRv6 L3 SID Locator Metric
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('srv6L3SidLocMetric'))

    @property
    def Srv6L3SidReserved(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SRv6 L3 SID Reserved Value (SRv6 SID Service TLV Level)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('srv6L3SidReserved'))

    @property
    def Srv6L3SidStep(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Route Range SRv6 SID Step
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('srv6L3SidStep'))

    @property
    def Srv6SIDOptionalInformation(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SRv6 L2 SID Optional Information field Value (Service Information sub-TLV) for all routes in this Route Range
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('srv6SIDOptionalInformation'))

    @property
    def Srv6SidReserved1(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SRv6 L2 SID Reserved1 Field for Service Information sub-TLV
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('srv6SidReserved1'))

    @property
    def Srv6SidReserved2(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SRv6 L2 SID Reserved2 Field for Service Information sub-TLV
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('srv6SidReserved2'))

    @property
    def UseSameSequenceNumber(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Use Same Sequence Number
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('useSameSequenceNumber'))

    def update(self, Name=None, NoOfASPathSegmentsPerRouteRange=None, NoOfClusters=None, NoOfCommunities=None, NoOfExtendedCommunity=None):
        """Updates cMacProperties resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NoOfASPathSegmentsPerRouteRange (number): Number Of AS Path Segments Per Route Range
        - NoOfClusters (number): Number of Clusters
        - NoOfCommunities (number): Number of Communities
        - NoOfExtendedCommunity (number): Number of Extended Communities

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(locals())

    def add(self, Name=None, NoOfASPathSegmentsPerRouteRange=None, NoOfClusters=None, NoOfCommunities=None, NoOfExtendedCommunity=None):
        """Adds a new cMacProperties resource on the server and adds it to the container.

        Args
        ----
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NoOfASPathSegmentsPerRouteRange (number): Number Of AS Path Segments Per Route Range
        - NoOfClusters (number): Number of Clusters
        - NoOfCommunities (number): Number of Communities
        - NoOfExtendedCommunity (number): Number of Extended Communities

        Returns
        -------
        - self: This instance with all currently retrieved cMacProperties resources using find and the newly added cMacProperties resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(locals())

    def remove(self):
        """Deletes all the contained cMacProperties resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Count=None, DescriptiveName=None, Mac=None, Name=None, NoOfASPathSegmentsPerRouteRange=None, NoOfClusters=None, NoOfCommunities=None, NoOfExtendedCommunity=None):
        """Finds and retrieves cMacProperties resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve cMacProperties resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all cMacProperties resources from the server.

        Args
        ----
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offers more context
        - Mac (list(str)): MAC addresses of the devices
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NoOfASPathSegmentsPerRouteRange (number): Number Of AS Path Segments Per Route Range
        - NoOfClusters (number): Number of Clusters
        - NoOfCommunities (number): Number of Communities
        - NoOfExtendedCommunity (number): Number of Extended Communities

        Returns
        -------
        - self: This instance with matching cMacProperties resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of cMacProperties data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the cMacProperties resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def get_device_ids(self, PortNames=None, Active=None, ActiveTs=None, AdvSrv6L2SidInIgp=None, AdvSrv6L3SidInIgp=None, AdvertiseIpv4Address=None, AdvertiseIpv6Address=None, AdvertiseSRv6L2SID=None, AdvertiseSRv6L3SID=None, AggregatorAs=None, AggregatorId=None, AsSetMode=None, EnableAggregatorId=None, EnableAsPathSegments=None, EnableAtomicAggregate=None, EnableCluster=None, EnableCommunity=None, EnableExtendedCommunity=None, EnableLocalPreference=None, EnableMultiExitDiscriminator=None, EnableNextHop=None, EnableOrigin=None, EnableOriginatorId=None, EnableSecondLabel=None, EnableStickyStaticFlag=None, EnableUserDefinedSequenceNumber=None, EviId=None, FirstLabelStart=None, IncludeDefaultGatewayExtendedCommunity=None, Ipv4AddressPrefixLength=None, Ipv4NextHop=None, Ipv6AddressPrefixLength=None, Ipv6NextHop=None, LabelMode=None, LabelStep=None, LocalPreference=None, MultiExitDiscriminator=None, Origin=None, OriginatorId=None, OverridePeerAsSetMode=None, PeerAddress=None, SecondLabelStart=None, SendSRv6SIDOptionalInfo=None, SequenceNumber=None, SetNextHop=None, SetNextHopIpType=None, Srv6EndpointBehavior=None, Srv6L2SidFlags=None, Srv6L2SidLoc=None, Srv6L2SidLocLen=None, Srv6L2SidLocMetric=None, Srv6L2SidReserved=None, Srv6L2SidStep=None, Srv6L3SidFlags=None, Srv6L3SidLoc=None, Srv6L3SidLocLen=None, Srv6L3SidLocMetric=None, Srv6L3SidReserved=None, Srv6L3SidStep=None, Srv6SIDOptionalInformation=None, Srv6SidReserved1=None, Srv6SidReserved2=None, UseSameSequenceNumber=None):
        """Base class infrastructure that gets a list of cMacProperties device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active
        - ActiveTs (str): optional regex of activeTs
        - AdvSrv6L2SidInIgp (str): optional regex of advSrv6L2SidInIgp
        - AdvSrv6L3SidInIgp (str): optional regex of advSrv6L3SidInIgp
        - AdvertiseIpv4Address (str): optional regex of advertiseIpv4Address
        - AdvertiseIpv6Address (str): optional regex of advertiseIpv6Address
        - AdvertiseSRv6L2SID (str): optional regex of advertiseSRv6L2SID
        - AdvertiseSRv6L3SID (str): optional regex of advertiseSRv6L3SID
        - AggregatorAs (str): optional regex of aggregatorAs
        - AggregatorId (str): optional regex of aggregatorId
        - AsSetMode (str): optional regex of asSetMode
        - EnableAggregatorId (str): optional regex of enableAggregatorId
        - EnableAsPathSegments (str): optional regex of enableAsPathSegments
        - EnableAtomicAggregate (str): optional regex of enableAtomicAggregate
        - EnableCluster (str): optional regex of enableCluster
        - EnableCommunity (str): optional regex of enableCommunity
        - EnableExtendedCommunity (str): optional regex of enableExtendedCommunity
        - EnableLocalPreference (str): optional regex of enableLocalPreference
        - EnableMultiExitDiscriminator (str): optional regex of enableMultiExitDiscriminator
        - EnableNextHop (str): optional regex of enableNextHop
        - EnableOrigin (str): optional regex of enableOrigin
        - EnableOriginatorId (str): optional regex of enableOriginatorId
        - EnableSecondLabel (str): optional regex of enableSecondLabel
        - EnableStickyStaticFlag (str): optional regex of enableStickyStaticFlag
        - EnableUserDefinedSequenceNumber (str): optional regex of enableUserDefinedSequenceNumber
        - EviId (str): optional regex of eviId
        - FirstLabelStart (str): optional regex of firstLabelStart
        - IncludeDefaultGatewayExtendedCommunity (str): optional regex of includeDefaultGatewayExtendedCommunity
        - Ipv4AddressPrefixLength (str): optional regex of ipv4AddressPrefixLength
        - Ipv4NextHop (str): optional regex of ipv4NextHop
        - Ipv6AddressPrefixLength (str): optional regex of ipv6AddressPrefixLength
        - Ipv6NextHop (str): optional regex of ipv6NextHop
        - LabelMode (str): optional regex of labelMode
        - LabelStep (str): optional regex of labelStep
        - LocalPreference (str): optional regex of localPreference
        - MultiExitDiscriminator (str): optional regex of multiExitDiscriminator
        - Origin (str): optional regex of origin
        - OriginatorId (str): optional regex of originatorId
        - OverridePeerAsSetMode (str): optional regex of overridePeerAsSetMode
        - PeerAddress (str): optional regex of peerAddress
        - SecondLabelStart (str): optional regex of secondLabelStart
        - SendSRv6SIDOptionalInfo (str): optional regex of sendSRv6SIDOptionalInfo
        - SequenceNumber (str): optional regex of sequenceNumber
        - SetNextHop (str): optional regex of setNextHop
        - SetNextHopIpType (str): optional regex of setNextHopIpType
        - Srv6EndpointBehavior (str): optional regex of srv6EndpointBehavior
        - Srv6L2SidFlags (str): optional regex of srv6L2SidFlags
        - Srv6L2SidLoc (str): optional regex of srv6L2SidLoc
        - Srv6L2SidLocLen (str): optional regex of srv6L2SidLocLen
        - Srv6L2SidLocMetric (str): optional regex of srv6L2SidLocMetric
        - Srv6L2SidReserved (str): optional regex of srv6L2SidReserved
        - Srv6L2SidStep (str): optional regex of srv6L2SidStep
        - Srv6L3SidFlags (str): optional regex of srv6L3SidFlags
        - Srv6L3SidLoc (str): optional regex of srv6L3SidLoc
        - Srv6L3SidLocLen (str): optional regex of srv6L3SidLocLen
        - Srv6L3SidLocMetric (str): optional regex of srv6L3SidLocMetric
        - Srv6L3SidReserved (str): optional regex of srv6L3SidReserved
        - Srv6L3SidStep (str): optional regex of srv6L3SidStep
        - Srv6SIDOptionalInformation (str): optional regex of srv6SIDOptionalInformation
        - Srv6SidReserved1 (str): optional regex of srv6SidReserved1
        - Srv6SidReserved2 (str): optional regex of srv6SidReserved2
        - UseSameSequenceNumber (str): optional regex of useSameSequenceNumber

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())

    def ReadvertiseCMac(self, *args, **kwargs):
        """Executes the readvertiseCMac operation on the server.

        Readvertise C-MAC

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        readvertiseCMac(SessionIndices=list)
        ------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

        readvertiseCMac(SessionIndices=string)
        --------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        readvertiseCMac(Arg2=list)list
        ------------------------------
        - Arg2 (list(number)): List of indices into the group. An empty list indicates all instances in the group.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('readvertiseCMac', payload=payload, response_object=None)

    def Start(self, *args, **kwargs):
        """Executes the start operation on the server.

        Start selected protocols.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        start(SessionIndices=list)
        --------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

        start(SessionIndices=string)
        ----------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('start', payload=payload, response_object=None)

    def Stop(self, *args, **kwargs):
        """Executes the stop operation on the server.

        Stop selected protocols.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        stop(SessionIndices=list)
        -------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

        stop(SessionIndices=string)
        ---------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('stop', payload=payload, response_object=None)
