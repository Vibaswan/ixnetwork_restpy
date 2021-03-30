# MIT LICENSE
#
# Copyright 1997 - 2020 by IXIA Keysight
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


class Ipv4(Base):
    """Static IPV4
    The Ipv4 class encapsulates a list of ipv4 resources that are managed by the user.
    A list of resources can be retrieved from the server using the Ipv4.find() method.
    The list can be managed by using the Ipv4.add() and Ipv4.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'ipv4'
    _SDM_ATT_MAP = {
        'Address': 'address',
        'ConnectedVia': 'connectedVia',
        'Count': 'count',
        'DescriptiveName': 'descriptiveName',
        'EnableGratarpRarp': 'enableGratarpRarp',
        'Errors': 'errors',
        'GatewayIp': 'gatewayIp',
        'Ipv4GratarpRarp': 'ipv4GratarpRarp',
        'ManualGatewayMac': 'manualGatewayMac',
        'Multiplier': 'multiplier',
        'Name': 'name',
        'Prefix': 'prefix',
        'ResolveGateway': 'resolveGateway',
        'ResolvedGatewayMac': 'resolvedGatewayMac',
        'SessionInfo': 'sessionInfo',
        'SessionStatus': 'sessionStatus',
        'StackedLayers': 'stackedLayers',
        'StateCounts': 'stateCounts',
        'Status': 'status',
    }

    def __init__(self, parent):
        super(Ipv4, self).__init__(parent)

    @property
    def Ancp(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ancp_32ef0f30885d45a86fb93ff8c22f3107.Ancp): An instance of the Ancp class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ancp_32ef0f30885d45a86fb93ff8c22f3107 import Ancp
        if self._properties.get('Ancp', None) is None:
            return Ancp(self)
        else:
            return self._properties.get('Ancp')

    @property
    def Bfdv4Interface(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bfdv4interface_91b557a3f744baf442dbe21ac75e8f2e.Bfdv4Interface): An instance of the Bfdv4Interface class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bfdv4interface_91b557a3f744baf442dbe21ac75e8f2e import Bfdv4Interface
        if self._properties.get('Bfdv4Interface', None) is None:
            return Bfdv4Interface(self)
        else:
            return self._properties.get('Bfdv4Interface')

    @property
    def BgpIpv4Peer(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpipv4peer_9dd9eddcf2bd784d82d8a016e392f035.BgpIpv4Peer): An instance of the BgpIpv4Peer class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpipv4peer_9dd9eddcf2bd784d82d8a016e392f035 import BgpIpv4Peer
        if self._properties.get('BgpIpv4Peer', None) is None:
            return BgpIpv4Peer(self)
        else:
            return self._properties.get('BgpIpv4Peer')

    @property
    def Dhcpv4relayAgent(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcpv4relayagent_f4cc56bb53d1903e9ec0dfc563d37d9c.Dhcpv4relayAgent): An instance of the Dhcpv4relayAgent class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcpv4relayagent_f4cc56bb53d1903e9ec0dfc563d37d9c import Dhcpv4relayAgent
        if self._properties.get('Dhcpv4relayAgent', None) is None:
            return Dhcpv4relayAgent(self)
        else:
            return self._properties.get('Dhcpv4relayAgent')

    @property
    def Dhcpv4server(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcpv4server_a0d174266d4c9a35774364ccc4dfccb3.Dhcpv4server): An instance of the Dhcpv4server class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcpv4server_a0d174266d4c9a35774364ccc4dfccb3 import Dhcpv4server
        if self._properties.get('Dhcpv4server', None) is None:
            return Dhcpv4server(self)
        else:
            return self._properties.get('Dhcpv4server')

    @property
    def ECpriRe(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ecprire_51f1030cbafd2e567d3b517032a1b011.ECpriRe): An instance of the ECpriRe class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ecprire_51f1030cbafd2e567d3b517032a1b011 import ECpriRe
        if self._properties.get('ECpriRe', None) is None:
            return ECpriRe(self)
        else:
            return self._properties.get('ECpriRe')

    @property
    def ECpriRec(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ecprirec_129f1d43f285a4f806ade4e0df814255.ECpriRec): An instance of the ECpriRec class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ecprirec_129f1d43f285a4f806ade4e0df814255 import ECpriRec
        if self._properties.get('ECpriRec', None) is None:
            return ECpriRec(self)
        else:
            return self._properties.get('ECpriRec')

    @property
    def Geneve(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.geneve_14ab6f140956b4fc77d1d0f03c5e7514.Geneve): An instance of the Geneve class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.geneve_14ab6f140956b4fc77d1d0f03c5e7514 import Geneve
        if self._properties.get('Geneve', None) is None:
            return Geneve(self)
        else:
            return self._properties.get('Geneve')

    @property
    def Greoipv4(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.greoipv4_47471ed6d75da2624c0a7f0801119b01.Greoipv4): An instance of the Greoipv4 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.greoipv4_47471ed6d75da2624c0a7f0801119b01 import Greoipv4
        if self._properties.get('Greoipv4', None) is None:
            return Greoipv4(self)
        else:
            return self._properties.get('Greoipv4')

    @property
    def IgmpHost(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.igmphost_8940887674c0387469423e8df3a33854.IgmpHost): An instance of the IgmpHost class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.igmphost_8940887674c0387469423e8df3a33854 import IgmpHost
        if self._properties.get('IgmpHost', None) is None:
            return IgmpHost(self)
        else:
            return self._properties.get('IgmpHost')

    @property
    def IgmpQuerier(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.igmpquerier_38c883b0cec7ffb5405af90bf1b8cda5.IgmpQuerier): An instance of the IgmpQuerier class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.igmpquerier_38c883b0cec7ffb5405af90bf1b8cda5 import IgmpQuerier
        if self._properties.get('IgmpQuerier', None) is None:
            return IgmpQuerier(self)
        else:
            return self._properties.get('IgmpQuerier')

    @property
    def Lac(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.lac_92ac6d7a9bf02ade5331532b27bfa0ea.Lac): An instance of the Lac class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.lac_92ac6d7a9bf02ade5331532b27bfa0ea import Lac
        if self._properties.get('Lac', None) is None:
            return Lac(self)
        else:
            return self._properties.get('Lac')

    @property
    def LdpBasicRouter(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldpbasicrouter_53e2de40003674322c811a1ba519dbb6.LdpBasicRouter): An instance of the LdpBasicRouter class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldpbasicrouter_53e2de40003674322c811a1ba519dbb6 import LdpBasicRouter
        if self._properties.get('LdpBasicRouter', None) is None:
            return LdpBasicRouter(self)
        else:
            return self._properties.get('LdpBasicRouter')

    @property
    def LdpConnectedInterface(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldpconnectedinterface_be8d40bb9f96a3d7371ddaf597237ff0.LdpConnectedInterface): An instance of the LdpConnectedInterface class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldpconnectedinterface_be8d40bb9f96a3d7371ddaf597237ff0 import LdpConnectedInterface
        if self._properties.get('LdpConnectedInterface', None) is None:
            return LdpConnectedInterface(self)
        else:
            return self._properties.get('LdpConnectedInterface')

    @property
    def LdpTargetedRouter(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldptargetedrouter_85c7a9993d80996c22a9dbd739df9692.LdpTargetedRouter): An instance of the LdpTargetedRouter class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldptargetedrouter_85c7a9993d80996c22a9dbd739df9692 import LdpTargetedRouter
        if self._properties.get('LdpTargetedRouter', None) is None:
            return LdpTargetedRouter(self)
        else:
            return self._properties.get('LdpTargetedRouter')

    @property
    def Lns(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.lns_a4b3be663ffb1dfb1f114cda5dbbcd4e.Lns): An instance of the Lns class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.lns_a4b3be663ffb1dfb1f114cda5dbbcd4e import Lns
        if self._properties.get('Lns', None) is None:
            return Lns(self)
        else:
            return self._properties.get('Lns')

    @property
    def MplsOam(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.mplsoam_e01bb6affe899a4731aa60619f4aeadc.MplsOam): An instance of the MplsOam class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.mplsoam_e01bb6affe899a4731aa60619f4aeadc import MplsOam
        if self._properties.get('MplsOam', None) is None:
            return MplsOam(self)
        else:
            return self._properties.get('MplsOam')

    @property
    def NetconfClient(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.netconfclient_1eaa2ab0efacd988796bdc1f5fe4291c.NetconfClient): An instance of the NetconfClient class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.netconfclient_1eaa2ab0efacd988796bdc1f5fe4291c import NetconfClient
        if self._properties.get('NetconfClient', None) is None:
            return NetconfClient(self)
        else:
            return self._properties.get('NetconfClient')

    @property
    def NetconfServer(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.netconfserver_ad256f8ca38068f1eaff839ed40b1e30.NetconfServer): An instance of the NetconfServer class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.netconfserver_ad256f8ca38068f1eaff839ed40b1e30 import NetconfServer
        if self._properties.get('NetconfServer', None) is None:
            return NetconfServer(self)
        else:
            return self._properties.get('NetconfServer')

    @property
    def Ntpclock(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ntpclock_0d879e81ae3d4c658c1fddb7e0bca059.Ntpclock): An instance of the Ntpclock class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ntpclock_0d879e81ae3d4c658c1fddb7e0bca059 import Ntpclock
        if self._properties.get('Ntpclock', None) is None:
            return Ntpclock(self)
        else:
            return self._properties.get('Ntpclock')

    @property
    def OpenFlowController(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.openflowcontroller_855b90b006cc4c874a779dee4d2b3eb2.OpenFlowController): An instance of the OpenFlowController class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.openflowcontroller_855b90b006cc4c874a779dee4d2b3eb2 import OpenFlowController
        if self._properties.get('OpenFlowController', None) is None:
            return OpenFlowController(self)
        else:
            return self._properties.get('OpenFlowController')

    @property
    def OpenFlowSwitch(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.openflowswitch_11d07d0a0b339c8fe20b86a2badffa69.OpenFlowSwitch): An instance of the OpenFlowSwitch class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.openflowswitch_11d07d0a0b339c8fe20b86a2badffa69 import OpenFlowSwitch
        if self._properties.get('OpenFlowSwitch', None) is None:
            return OpenFlowSwitch(self)
        else:
            return self._properties.get('OpenFlowSwitch')

    @property
    def Ospfv2(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfv2_27b7a27a991a50e01e629b9de482a2f0.Ospfv2): An instance of the Ospfv2 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfv2_27b7a27a991a50e01e629b9de482a2f0 import Ospfv2
        if self._properties.get('Ospfv2', None) is None:
            return Ospfv2(self)
        else:
            return self._properties.get('Ospfv2')

    @property
    def Ovsdbcontroller(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ovsdbcontroller_789ff2911c009a5ce719da4041ccbf73.Ovsdbcontroller): An instance of the Ovsdbcontroller class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ovsdbcontroller_789ff2911c009a5ce719da4041ccbf73 import Ovsdbcontroller
        if self._properties.get('Ovsdbcontroller', None) is None:
            return Ovsdbcontroller(self)
        else:
            return self._properties.get('Ovsdbcontroller')

    @property
    def Ovsdbserver(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ovsdbserver_54c04aa8692b2b034dcd8eac05978340.Ovsdbserver): An instance of the Ovsdbserver class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ovsdbserver_54c04aa8692b2b034dcd8eac05978340 import Ovsdbserver
        if self._properties.get('Ovsdbserver', None) is None:
            return Ovsdbserver(self)
        else:
            return self._properties.get('Ovsdbserver')

    @property
    def Pcc(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pcc_9346785b55d17399fecd6fe36c418219.Pcc): An instance of the Pcc class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pcc_9346785b55d17399fecd6fe36c418219 import Pcc
        if self._properties.get('Pcc', None) is None:
            return Pcc(self)
        else:
            return self._properties.get('Pcc')

    @property
    def Pce(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pce_bd5f6a11078a4f0deb5d56bef8e9674f.Pce): An instance of the Pce class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pce_bd5f6a11078a4f0deb5d56bef8e9674f import Pce
        if self._properties.get('Pce', None) is None:
            return Pce(self)
        else:
            return self._properties.get('Pce')

    @property
    def PimV4Interface(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pimv4interface_92603cbceaf153039f7575ed9bc4aa67.PimV4Interface): An instance of the PimV4Interface class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pimv4interface_92603cbceaf153039f7575ed9bc4aa67 import PimV4Interface
        if self._properties.get('PimV4Interface', None) is None:
            return PimV4Interface(self)
        else:
            return self._properties.get('PimV4Interface')

    @property
    def Ptp(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ptp_26111dde679ed88af879687d76db2401.Ptp): An instance of the Ptp class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ptp_26111dde679ed88af879687d76db2401 import Ptp
        if self._properties.get('Ptp', None) is None:
            return Ptp(self)
        else:
            return self._properties.get('Ptp')

    @property
    def RsvpteIf(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.rsvpteif_e2b2ecdbf1fa5e15d2f6d87dd1789f1c.RsvpteIf): An instance of the RsvpteIf class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.rsvpteif_e2b2ecdbf1fa5e15d2f6d87dd1789f1c import RsvpteIf
        if self._properties.get('RsvpteIf', None) is None:
            return RsvpteIf(self)
        else:
            return self._properties.get('RsvpteIf')

    @property
    def RsvpteLsps(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.rsvptelsps_c853570a71a8549c854868139dd47959.RsvpteLsps): An instance of the RsvpteLsps class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.rsvptelsps_c853570a71a8549c854868139dd47959 import RsvpteLsps
        if self._properties.get('RsvpteLsps', None) is None:
            return RsvpteLsps(self)
        else:
            return self._properties.get('RsvpteLsps')

    @property
    def Tag(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.tag_e30f24de79247381d4dfd423b2f6986d.Tag): An instance of the Tag class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.tag_e30f24de79247381d4dfd423b2f6986d import Tag
        if self._properties.get('Tag', None) is None:
            return Tag(self)
        else:
            return self._properties.get('Tag')

    @property
    def Vxlan(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.vxlan_ed3df6fe7146492fc5fe0f77f53f9473.Vxlan): An instance of the Vxlan class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.vxlan_ed3df6fe7146492fc5fe0f77f53f9473 import Vxlan
        if self._properties.get('Vxlan', None) is None:
            return Vxlan(self)
        else:
            return self._properties.get('Vxlan')

    @property
    def Address(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IPv4 addresses of the devices
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Address']))

    @property
    def ConnectedVia(self):
        """DEPRECATED 
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*]): List of layers this layer is used to connect with to the wire.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ConnectedVia'])
    @ConnectedVia.setter
    def ConnectedVia(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ConnectedVia'], value)

    @property
    def Count(self):
        """
        Returns
        -------
        - number: Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Count'])

    @property
    def DescriptiveName(self):
        """
        Returns
        -------
        - str: Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DescriptiveName'])

    @property
    def EnableGratarpRarp(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enables GRATARP or RARP packet transmission.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableGratarpRarp']))

    @property
    def Errors(self):
        """
        Returns
        -------
        - list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork//.../*],arg2:list[str])): A list of errors that have occurred
        """
        return self._get_attribute(self._SDM_ATT_MAP['Errors'])

    @property
    def GatewayIp(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IPv4 addresses of the Gateways for the devices
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['GatewayIp']))

    @property
    def Ipv4GratarpRarp(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Sends GRATARP or RARP packet.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Ipv4GratarpRarp']))

    @property
    def ManualGatewayMac(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): User specified Gateway MAC addresses
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ManualGatewayMac']))

    @property
    def Multiplier(self):
        """
        Returns
        -------
        - number: Number of layer instances per parent instance (multiplier)
        """
        return self._get_attribute(self._SDM_ATT_MAP['Multiplier'])
    @Multiplier.setter
    def Multiplier(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Multiplier'], value)

    @property
    def Name(self):
        """
        Returns
        -------
        - str: Name of NGPF element, guaranteed to be unique in Scenario
        """
        return self._get_attribute(self._SDM_ATT_MAP['Name'])
    @Name.setter
    def Name(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Name'], value)

    @property
    def Prefix(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The length (in bits) of the mask to be used in conjunction with all the addresses created in the range
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Prefix']))

    @property
    def ResolveGateway(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enables the gateway MAC address discovery.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ResolveGateway']))

    @property
    def ResolvedGatewayMac(self):
        """
        Returns
        -------
        - list(str): The resolved gateway's MAC addresses
        """
        return self._get_attribute(self._SDM_ATT_MAP['ResolvedGatewayMac'])

    @property
    def SessionInfo(self):
        """
        Returns
        -------
        - list(str[interfaceRemoved | none | resolveMacFailed]): Logs additional information about the session state.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SessionInfo'])

    @property
    def SessionStatus(self):
        """
        Returns
        -------
        - list(str[down | notStarted | up]): Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SessionStatus'])

    @property
    def StackedLayers(self):
        """
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*]): List of secondary (many to one) child layer protocols
        """
        return self._get_attribute(self._SDM_ATT_MAP['StackedLayers'])
    @StackedLayers.setter
    def StackedLayers(self, value):
        self._set_attribute(self._SDM_ATT_MAP['StackedLayers'], value)

    @property
    def StateCounts(self):
        """
        Returns
        -------
        - dict(total:number,notStarted:number,down:number,up:number): A list of values that indicates the total number of sessions, the number of sessions not started, the number of sessions down and the number of sessions that are up
        """
        return self._get_attribute(self._SDM_ATT_MAP['StateCounts'])

    @property
    def Status(self):
        """
        Returns
        -------
        - str(configured | error | mixed | notStarted | started | starting | stopping): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Status'])

    def update(self, ConnectedVia=None, Multiplier=None, Name=None, StackedLayers=None):
        """Updates ipv4 resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of layers this layer is used to connect with to the wire.
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of secondary (many to one) child layer protocols

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, ConnectedVia=None, Multiplier=None, Name=None, StackedLayers=None):
        """Adds a new ipv4 resource on the server and adds it to the container.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of layers this layer is used to connect with to the wire.
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of secondary (many to one) child layer protocols

        Returns
        -------
        - self: This instance with all currently retrieved ipv4 resources using find and the newly added ipv4 resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained ipv4 resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, ConnectedVia=None, Count=None, DescriptiveName=None, Errors=None, Multiplier=None, Name=None, ResolvedGatewayMac=None, SessionInfo=None, SessionStatus=None, StackedLayers=None, StateCounts=None, Status=None):
        """Finds and retrieves ipv4 resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve ipv4 resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all ipv4 resources from the server.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of layers this layer is used to connect with to the wire.
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - Errors (list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork//.../*],arg2:list[str]))): A list of errors that have occurred
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - ResolvedGatewayMac (list(str)): The resolved gateway's MAC addresses
        - SessionInfo (list(str[interfaceRemoved | none | resolveMacFailed])): Logs additional information about the session state.
        - SessionStatus (list(str[down | notStarted | up])): Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of secondary (many to one) child layer protocols
        - StateCounts (dict(total:number,notStarted:number,down:number,up:number)): A list of values that indicates the total number of sessions, the number of sessions not started, the number of sessions down and the number of sessions that are up
        - Status (str(configured | error | mixed | notStarted | started | starting | stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.

        Returns
        -------
        - self: This instance with matching ipv4 resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of ipv4 data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the ipv4 resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def get_device_ids(self, PortNames=None, Address=None, EnableGratarpRarp=None, GatewayIp=None, Ipv4GratarpRarp=None, ManualGatewayMac=None, Prefix=None, ResolveGateway=None):
        """Base class infrastructure that gets a list of ipv4 device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Address (str): optional regex of address
        - EnableGratarpRarp (str): optional regex of enableGratarpRarp
        - GatewayIp (str): optional regex of gatewayIp
        - Ipv4GratarpRarp (str): optional regex of ipv4GratarpRarp
        - ManualGatewayMac (str): optional regex of manualGatewayMac
        - Prefix (str): optional regex of prefix
        - ResolveGateway (str): optional regex of resolveGateway

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())

    def Abort(self, *args, **kwargs):
        """Executes the abort operation on the server.

        Abort CPF control plane (equals to demote to kUnconfigured state).

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        abort(SessionIndices=list)
        --------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        abort(SessionIndices=string)
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
        return self._execute('abort', payload=payload, response_object=None)

    def FetchAndUpdateConfigFromCloud(self, *args, **kwargs):
        """Executes the fetchAndUpdateConfigFromCloud operation on the server.

        Learn MAC / IP address for a topology running on VM ports, deployed in AWS.

        fetchAndUpdateConfigFromCloud(Mode=string)
        ------------------------------------------
        - Mode (str): Mode. Options are: cmdrefreshall, cmdrefreshmac, cmdrefreshipv4

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('fetchAndUpdateConfigFromCloud', payload=payload, response_object=None)

    def RestartDown(self, *args, **kwargs):
        """Executes the restartDown operation on the server.

        Stop and start interfaces and sessions that are in Down state.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        restartDown(SessionIndices=list)
        --------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

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

    def SendArp(self, *args, **kwargs):
        """Executes the sendArp operation on the server.

        Send ARP request to configured gateway IP to resolve Gateway MAC for selected items.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        sendArp(SessionIndices=list)
        ----------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        sendArp(SessionIndices=string)
        ------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('sendArp', payload=payload, response_object=None)

    def SendArpManual(self, *args, **kwargs):
        """Executes the sendArpManual operation on the server.

        Send ARP request to specified IP for selected IPv4 items.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        sendArpManual(DestIP=string)list
        --------------------------------
        - DestIP (str): This parameter requires a destIP of type kString
        - Returns list(dict(port:str[None | /api/v1/sessions/1/ixnetwork/vport],isSuccess:bool,data:str)): The return value is an array of structures where each structure consists of a /vport object reference, the success of the operation and the returned data of the operation for that /vport. This exec is not asynchronous.

        sendArpManual(DestIP=string, SessionIndices=list)list
        -----------------------------------------------------
        - DestIP (str): This parameter requires a destIP of type kString
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - Returns list(dict(port:str[None | /api/v1/sessions/1/ixnetwork/vport],isSuccess:bool,data:str)): The return value is an array of structures where each structure consists of a /vport object reference, the success of the operation and the returned data of the operation for that /vport. This exec is not asynchronous.

        sendArpManual(SessionIndices=string, DestIP=string)list
        -------------------------------------------------------
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
        return self._execute('sendArpManual', payload=payload, response_object=None)

    def SendGratArp(self, *args, **kwargs):
        """Executes the sendGratArp operation on the server.

        Sends GRATARP request to specified source IP for selected IPv4 items.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        sendGratArp(SessionIndices=list)
        --------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        sendGratArp(SessionIndices=string)
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
        return self._execute('sendGratArp', payload=payload, response_object=None)

    def SendPing(self, *args, **kwargs):
        """Executes the sendPing operation on the server.

        Send ping for selected IPv4 items.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        sendPing(DestIP=string)list
        ---------------------------
        - DestIP (str): This parameter requires a destIP of type kString
        - Returns list(dict(port:str[None | /api/v1/sessions/1/ixnetwork/vport],isSuccess:bool,data:str)): The return value is an array of structures where each structure consists of a /vport object reference, the success of the operation and the returned data of the operation for that /vport. This exec is not asynchronous.

        sendPing(DestIP=string, SessionIndices=list)list
        ------------------------------------------------
        - DestIP (str): This parameter requires a destIP of type kString
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
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

    def SendRarp(self, *args, **kwargs):
        """Executes the sendRarp operation on the server.

        Sends RARP request to specified source IP for selected IPv4 items.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        sendRarp(SessionIndices=list)
        -----------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        sendRarp(SessionIndices=string)
        -------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('sendRarp', payload=payload, response_object=None)

    def Start(self, *args, **kwargs):
        """Executes the start operation on the server.

        Start CPF control plane (equals to promote to negotiated state).

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        start(SessionIndices=list)
        --------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

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

        Stop CPF control plane (equals to demote to PreValidated-DoDDone state).

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        stop(SessionIndices=list)
        -------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

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
