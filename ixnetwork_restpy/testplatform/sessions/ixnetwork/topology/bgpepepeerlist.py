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


class BgpEpePeerList(Base):
    """EPE Peers
    The BgpEpePeerList class encapsulates a required bgpEpePeerList resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'bgpEpePeerList'

    def __init__(self, parent):
        super(BgpEpePeerList, self).__init__(parent)

    @property
    def BgpEpePeerLinkList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpepepeerlinklist.BgpEpePeerLinkList): An instance of the BgpEpePeerLinkList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpepepeerlinklist import BgpEpePeerLinkList
        return BgpEpePeerLinkList(self)._select()

    @property
    def BgpEpePeerSetList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpepepeersetlist.BgpEpePeerSetList): An instance of the BgpEpePeerSetList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpepepeersetlist import BgpEpePeerSetList
        return BgpEpePeerSetList(self)

    @property
    def Active(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Activate/Deactivate Configuration.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('active'))

    @property
    def BBit(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): B-Flag:Backup Flag.If set, the SID refers to a path that is eligible for protection.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('bBit'))

    @property
    def BgpLocalRouterId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): BGP Router ID for Local Node Descriptor
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('bgpLocalRouterId'))

    @property
    def BgpRemoteRouterId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): BGP Router ID for Remote Node Descriptor
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('bgpRemoteRouterId'))

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
    def EnablePeerNodeSid(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Peer-Node-SID
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('enablePeerNodeSid'))

    @property
    def LBit(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): L-Flag: Local Flag. If set, then the value/index carried by the SID has local significance.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('lBit'))

    @property
    def LocalAsn(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): AS# of Egress node
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('localAsn'))

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
    def NoOfPeerSet(self):
        """
        Returns
        -------
        - number: Number of EPE Peer Set
        """
        return self._get_attribute('noOfPeerSet')
    @NoOfPeerSet.setter
    def NoOfPeerSet(self, value):
        self._set_attribute('noOfPeerSet', value)

    @property
    def NoOflinks(self):
        """
        Returns
        -------
        - number: Number of Links
        """
        return self._get_attribute('noOflinks')
    @NoOflinks.setter
    def NoOflinks(self, value):
        self._set_attribute('noOflinks', value)

    @property
    def PBit(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): P-Flag: Persistent Flag: If set, the SID is persistently allocated, i.e. the SID value remains consistent across router restart and session/interface flap
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('pBit'))

    @property
    def PeerName(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Peer Name For Reference
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('peerName'))

    @property
    def PeerSetGroup(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Peer Set Group
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('peerSetGroup'))

    @property
    def RemoteAsn(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): AS# of Peer Node
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('remoteAsn'))

    @property
    def Reserved(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Reserved
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('reserved'))

    @property
    def RsvdBits(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Reserved for future use and MUST be zero when originated and ignored when received
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('rsvdBits'))

    @property
    def SidIndex(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Local Label for Peer-Node
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('sidIndex'))

    @property
    def SidIndexValue(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If Local Label type is SID, max value is 16777215 and for Index max value is 4294967295
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('sidIndexValue'))

    @property
    def UseLocalConfedId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Use Local Confederation identifier
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('useLocalConfedId'))

    @property
    def UseRemoteConfedId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Use Remote Confederation identifier
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('useRemoteConfedId'))

    @property
    def VBit(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): V-Flag: Value flag. If set, then the SID carries a label value.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('vBit'))

    @property
    def Weight(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Weight of SID for Load Balancing
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('weight'))

    def update(self, Name=None, NoOfPeerSet=None, NoOflinks=None):
        """Updates bgpEpePeerList resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NoOfPeerSet (number): Number of EPE Peer Set
        - NoOflinks (number): Number of Links

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(locals())

    def get_device_ids(self, PortNames=None, Active=None, BBit=None, BgpLocalRouterId=None, BgpRemoteRouterId=None, EnablePeerNodeSid=None, LBit=None, LocalAsn=None, PBit=None, PeerName=None, PeerSetGroup=None, RemoteAsn=None, Reserved=None, RsvdBits=None, SidIndex=None, SidIndexValue=None, UseLocalConfedId=None, UseRemoteConfedId=None, VBit=None, Weight=None):
        """Base class infrastructure that gets a list of bgpEpePeerList device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active
        - BBit (str): optional regex of bBit
        - BgpLocalRouterId (str): optional regex of bgpLocalRouterId
        - BgpRemoteRouterId (str): optional regex of bgpRemoteRouterId
        - EnablePeerNodeSid (str): optional regex of enablePeerNodeSid
        - LBit (str): optional regex of lBit
        - LocalAsn (str): optional regex of localAsn
        - PBit (str): optional regex of pBit
        - PeerName (str): optional regex of peerName
        - PeerSetGroup (str): optional regex of peerSetGroup
        - RemoteAsn (str): optional regex of remoteAsn
        - Reserved (str): optional regex of reserved
        - RsvdBits (str): optional regex of rsvdBits
        - SidIndex (str): optional regex of sidIndex
        - SidIndexValue (str): optional regex of sidIndexValue
        - UseLocalConfedId (str): optional regex of useLocalConfedId
        - UseRemoteConfedId (str): optional regex of useRemoteConfedId
        - VBit (str): optional regex of vBit
        - Weight (str): optional regex of weight

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
