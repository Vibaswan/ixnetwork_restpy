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


class Ipv4Loopback(Base):
    """IPv4 Loopback
    The Ipv4Loopback class encapsulates a list of ipv4Loopback resources that are managed by the user.
    A list of resources can be retrieved from the server using the Ipv4Loopback.find() method.
    The list can be managed by using the Ipv4Loopback.add() and Ipv4Loopback.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'ipv4Loopback'

    def __init__(self, parent):
        super(Ipv4Loopback, self).__init__(parent)

    @property
    def Bfdv4Interface(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bfdv4interface.Bfdv4Interface): An instance of the Bfdv4Interface class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bfdv4interface import Bfdv4Interface
        return Bfdv4Interface(self)

    @property
    def BgpIpv4Peer(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpipv4peer.BgpIpv4Peer): An instance of the BgpIpv4Peer class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpipv4peer import BgpIpv4Peer
        return BgpIpv4Peer(self)

    @property
    def Connector(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.connector.Connector): An instance of the Connector class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.connector import Connector
        return Connector(self)

    @property
    def ECpriRe(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ecprire.ECpriRe): An instance of the ECpriRe class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ecprire import ECpriRe
        return ECpriRe(self)

    @property
    def ECpriRec(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ecprirec.ECpriRec): An instance of the ECpriRec class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ecprirec import ECpriRec
        return ECpriRec(self)

    @property
    def Geneve(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.geneve.Geneve): An instance of the Geneve class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.geneve import Geneve
        return Geneve(self)

    @property
    def Greoipv4(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.greoipv4.Greoipv4): An instance of the Greoipv4 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.greoipv4 import Greoipv4
        return Greoipv4(self)

    @property
    def IgmpHost(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.igmphost.IgmpHost): An instance of the IgmpHost class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.igmphost import IgmpHost
        return IgmpHost(self)

    @property
    def IgmpQuerier(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.igmpquerier.IgmpQuerier): An instance of the IgmpQuerier class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.igmpquerier import IgmpQuerier
        return IgmpQuerier(self)

    @property
    def LdpTargetedRouter(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldptargetedrouter.LdpTargetedRouter): An instance of the LdpTargetedRouter class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldptargetedrouter import LdpTargetedRouter
        return LdpTargetedRouter(self)

    @property
    def MplsOam(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.mplsoam.MplsOam): An instance of the MplsOam class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.mplsoam import MplsOam
        return MplsOam(self)

    @property
    def NetconfClient(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.netconfclient.NetconfClient): An instance of the NetconfClient class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.netconfclient import NetconfClient
        return NetconfClient(self)

    @property
    def NetconfServer(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.netconfserver.NetconfServer): An instance of the NetconfServer class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.netconfserver import NetconfServer
        return NetconfServer(self)

    @property
    def Ntpclock(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ntpclock.Ntpclock): An instance of the Ntpclock class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ntpclock import Ntpclock
        return Ntpclock(self)

    @property
    def Ospfv2(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfv2.Ospfv2): An instance of the Ospfv2 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfv2 import Ospfv2
        return Ospfv2(self)

    @property
    def Pcc(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pcc.Pcc): An instance of the Pcc class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pcc import Pcc
        return Pcc(self)

    @property
    def Pce(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pce.Pce): An instance of the Pce class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pce import Pce
        return Pce(self)

    @property
    def PimV4Interface(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pimv4interface.PimV4Interface): An instance of the PimV4Interface class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pimv4interface import PimV4Interface
        return PimV4Interface(self)

    @property
    def RsvpteLsps(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.rsvptelsps.RsvpteLsps): An instance of the RsvpteLsps class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.rsvptelsps import RsvpteLsps
        return RsvpteLsps(self)

    @property
    def Tag(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.tag.Tag): An instance of the Tag class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.tag import Tag
        return Tag(self)

    @property
    def Vxlan(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.vxlan.Vxlan): An instance of the Vxlan class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.vxlan import Vxlan
        return Vxlan(self)

    @property
    def Address(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IPv4 addresses of the devices
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('address'))

    @property
    def ConnectedVia(self):
        """DEPRECATED 
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*]): List of layers this layer used to connect to the wire
        """
        return self._get_attribute('connectedVia')
    @ConnectedVia.setter
    def ConnectedVia(self, value):
        self._set_attribute('connectedVia', value)

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
    def Errors(self):
        """
        Returns
        -------
        - list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork//.../*],arg2:list[str])): A list of errors that have occurred
        """
        return self._get_attribute('errors')

    @property
    def Multiplier(self):
        """
        Returns
        -------
        - number: Number of layer instances per parent instance (multiplier)
        """
        return self._get_attribute('multiplier')
    @Multiplier.setter
    def Multiplier(self, value):
        self._set_attribute('multiplier', value)

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
    def Prefix(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The length (in bits) of the mask to be used in conjunction with all the addresses created in the range
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('prefix'))

    @property
    def SessionStatus(self):
        """
        Returns
        -------
        - list(str[down | notStarted | up]): Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.
        """
        return self._get_attribute('sessionStatus')

    @property
    def StackedLayers(self):
        """
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*]): List of secondary (many to one) child layer protocols
        """
        return self._get_attribute('stackedLayers')
    @StackedLayers.setter
    def StackedLayers(self, value):
        self._set_attribute('stackedLayers', value)

    @property
    def StateCounts(self):
        """
        Returns
        -------
        - dict(total:number,notStarted:number,down:number,up:number): A list of values that indicates the total number of sessions, the number of sessions not started, the number of sessions down and the number of sessions that are up
        """
        return self._get_attribute('stateCounts')

    @property
    def Status(self):
        """
        Returns
        -------
        - str(configured | error | mixed | notStarted | started | starting | stopping): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
        """
        return self._get_attribute('status')

    def update(self, ConnectedVia=None, Multiplier=None, Name=None, StackedLayers=None):
        """Updates ipv4Loopback resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of layers this layer used to connect to the wire
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of secondary (many to one) child layer protocols

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(locals())

    def add(self, ConnectedVia=None, Multiplier=None, Name=None, StackedLayers=None):
        """Adds a new ipv4Loopback resource on the server and adds it to the container.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of layers this layer used to connect to the wire
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of secondary (many to one) child layer protocols

        Returns
        -------
        - self: This instance with all currently retrieved ipv4Loopback resources using find and the newly added ipv4Loopback resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(locals())

    def remove(self):
        """Deletes all the contained ipv4Loopback resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, ConnectedVia=None, Count=None, DescriptiveName=None, Errors=None, Multiplier=None, Name=None, SessionStatus=None, StackedLayers=None, StateCounts=None, Status=None):
        """Finds and retrieves ipv4Loopback resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve ipv4Loopback resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all ipv4Loopback resources from the server.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of layers this layer used to connect to the wire
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offers more context
        - Errors (list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork//.../*],arg2:list[str]))): A list of errors that have occurred
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - SessionStatus (list(str[down | notStarted | up])): Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of secondary (many to one) child layer protocols
        - StateCounts (dict(total:number,notStarted:number,down:number,up:number)): A list of values that indicates the total number of sessions, the number of sessions not started, the number of sessions down and the number of sessions that are up
        - Status (str(configured | error | mixed | notStarted | started | starting | stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.

        Returns
        -------
        - self: This instance with matching ipv4Loopback resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of ipv4Loopback data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the ipv4Loopback resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def get_device_ids(self, PortNames=None, Address=None, Prefix=None):
        """Base class infrastructure that gets a list of ipv4Loopback device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Address (str): optional regex of address
        - Prefix (str): optional regex of prefix

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())

    def RestartDown(self, *args, **kwargs):
        """Executes the restartDown operation on the server.

        Stop and start interfaces and sessions that are in Down state.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        restartDown(SessionIndices=list)
        --------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

        restartDown(SessionIndices=string)
        ----------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('restartDown', payload=payload, response_object=None)

    def SendPing(self, *args, **kwargs):
        """Executes the sendPing operation on the server.

        Send ping for selected IPv4 Loopback items.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        sendPing(DestIP=string)list
        ---------------------------
        - DestIP (str): This parameter requires a destIP of type kString
        - Returns list(dict(port:str[None | /api/v1/sessions/1/ixnetwork/vport],isSuccess:bool,data:str)): The return value is an array of structures where each structure consists of a /vport object reference, the success of the operation and the returned data of the operation for that /vport. This exec is not asynchronous.

        sendPing(DestIP=string, SessionIndices=list)list
        ------------------------------------------------
        - DestIP (str): This parameter requires a destIP of type kString
        - SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3
        - Returns list(dict(port:str[None | /api/v1/sessions/1/ixnetwork/vport],isSuccess:bool,data:str)): The return value is an array of structures where each structure consists of a /vport object reference, the success of the operation and the returned data of the operation for that /vport. This exec is not asynchronous.

        sendPing(SessionIndices=string, DestIP=string)list
        --------------------------------------------------
        - SessionIndices (str): This parameter requires a destIP of type kString
        - DestIP (str): This parameter requires a string of session numbers 1-4;6;7-12
        - Returns list(dict(port:str[None | /api/v1/sessions/1/ixnetwork/vport],isSuccess:bool,data:str)): The return value is an array of structures where each structure consists of a /vport object reference, the success of the operation and the returned data of the operation for that /vport. This exec is not asynchronous.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('sendPing', payload=payload, response_object=None)

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
