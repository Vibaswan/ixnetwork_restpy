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


class ProtocolStack(Base):
    """PortGroup represents the concept of a stack of layers which are to be configured on a group of ports.
    The ProtocolStack class encapsulates a required protocolStack resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'protocolStack'
    _SDM_ATT_MAP = {
        'ObjectId': 'objectId',
    }

    def __init__(self, parent):
        super(ProtocolStack, self).__init__(parent)

    @property
    def AmtOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.amtoptions_920d5afd3e8b6201245458975a82c0db.AmtOptions): An instance of the AmtOptions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.amtoptions_920d5afd3e8b6201245458975a82c0db import AmtOptions
        if self._properties.get('AmtOptions', None) is None:
            return AmtOptions(self)
        else:
            return self._properties.get('AmtOptions')

    @property
    def AncpOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.ancpoptions_f260f6494b4e2ad033aeceec23cac54c.AncpOptions): An instance of the AncpOptions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.ancpoptions_f260f6494b4e2ad033aeceec23cac54c import AncpOptions
        if self._properties.get('AncpOptions', None) is None:
            return AncpOptions(self)
        else:
            return self._properties.get('AncpOptions')

    @property
    def DhcpHostsOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dhcphostsoptions_1aa84c4d3616ee0c49f129eb60e368f5.DhcpHostsOptions): An instance of the DhcpHostsOptions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dhcphostsoptions_1aa84c4d3616ee0c49f129eb60e368f5 import DhcpHostsOptions
        if self._properties.get('DhcpHostsOptions', None) is None:
            return DhcpHostsOptions(self)
        else:
            return self._properties.get('DhcpHostsOptions')

    @property
    def DhcpOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dhcpoptions_26f3d4f3f49721f70d8d3209df521d26.DhcpOptions): An instance of the DhcpOptions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dhcpoptions_26f3d4f3f49721f70d8d3209df521d26 import DhcpOptions
        if self._properties.get('DhcpOptions', None) is None:
            return DhcpOptions(self)
        else:
            return self._properties.get('DhcpOptions')

    @property
    def Dhcpv6ClientOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dhcpv6clientoptions_b7c7438f131dab8b0781a2aab896c6bf.Dhcpv6ClientOptions): An instance of the Dhcpv6ClientOptions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dhcpv6clientoptions_b7c7438f131dab8b0781a2aab896c6bf import Dhcpv6ClientOptions
        if self._properties.get('Dhcpv6ClientOptions', None) is None:
            return Dhcpv6ClientOptions(self)
        else:
            return self._properties.get('Dhcpv6ClientOptions')

    @property
    def Dhcpv6PdClientOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dhcpv6pdclientoptions_ca2a2ece3298de61d5b8bdd7a850035f.Dhcpv6PdClientOptions): An instance of the Dhcpv6PdClientOptions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dhcpv6pdclientoptions_ca2a2ece3298de61d5b8bdd7a850035f import Dhcpv6PdClientOptions
        if self._properties.get('Dhcpv6PdClientOptions', None) is None:
            return Dhcpv6PdClientOptions(self)
        else:
            return self._properties.get('Dhcpv6PdClientOptions')

    @property
    def Dhcpv6ServerOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dhcpv6serveroptions_a3f49164e013779eb52f1890d0a76869.Dhcpv6ServerOptions): An instance of the Dhcpv6ServerOptions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dhcpv6serveroptions_a3f49164e013779eb52f1890d0a76869 import Dhcpv6ServerOptions
        if self._properties.get('Dhcpv6ServerOptions', None) is None:
            return Dhcpv6ServerOptions(self)
        else:
            return self._properties.get('Dhcpv6ServerOptions')

    @property
    def Dot1xOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dot1xoptions_8a46299312ed9582fb7d7b160232f3c4.Dot1xOptions): An instance of the Dot1xOptions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dot1xoptions_8a46299312ed9582fb7d7b160232f3c4 import Dot1xOptions
        if self._properties.get('Dot1xOptions', None) is None:
            return Dot1xOptions(self)
        else:
            return self._properties.get('Dot1xOptions')

    @property
    def EapoUdpOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.eapoudpoptions_c637c5c5d1e6ed49fb44ea5297e78110.EapoUdpOptions): An instance of the EapoUdpOptions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.eapoudpoptions_c637c5c5d1e6ed49fb44ea5297e78110 import EapoUdpOptions
        if self._properties.get('EapoUdpOptions', None) is None:
            return EapoUdpOptions(self)
        else:
            return self._properties.get('EapoUdpOptions')

    @property
    def EgtpClientOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.egtpclientoptions_faed49d1cd6032d1d86c972d66b3a5fe.EgtpClientOptions): An instance of the EgtpClientOptions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.egtpclientoptions_faed49d1cd6032d1d86c972d66b3a5fe import EgtpClientOptions
        if self._properties.get('EgtpClientOptions', None) is None:
            return EgtpClientOptions(self)
        else:
            return self._properties.get('EgtpClientOptions')

    @property
    def EgtpOptionsBase(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.egtpoptionsbase_2c116dc95d43ffef03c94ddbd3b750be.EgtpOptionsBase): An instance of the EgtpOptionsBase class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.egtpoptionsbase_2c116dc95d43ffef03c94ddbd3b750be import EgtpOptionsBase
        if self._properties.get('EgtpOptionsBase', None) is None:
            return EgtpOptionsBase(self)
        else:
            return self._properties.get('EgtpOptionsBase')

    @property
    def EgtpS5S8PgwOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.egtps5s8pgwoptions_0ecee2b136b9e205c98c111ae43d2529.EgtpS5S8PgwOptions): An instance of the EgtpS5S8PgwOptions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.egtps5s8pgwoptions_0ecee2b136b9e205c98c111ae43d2529 import EgtpS5S8PgwOptions
        if self._properties.get('EgtpS5S8PgwOptions', None) is None:
            return EgtpS5S8PgwOptions(self)
        else:
            return self._properties.get('EgtpS5S8PgwOptions')

    @property
    def EgtpS5S8SgwOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.egtps5s8sgwoptions_85e0aea713fb798872e1eb8bc6544fe9.EgtpS5S8SgwOptions): An instance of the EgtpS5S8SgwOptions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.egtps5s8sgwoptions_85e0aea713fb798872e1eb8bc6544fe9 import EgtpS5S8SgwOptions
        if self._properties.get('EgtpS5S8SgwOptions', None) is None:
            return EgtpS5S8SgwOptions(self)
        else:
            return self._properties.get('EgtpS5S8SgwOptions')

    @property
    def EgtpServerOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.egtpserveroptions_0da9d0ef7484fcc78603ede124e9e586.EgtpServerOptions): An instance of the EgtpServerOptions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.egtpserveroptions_0da9d0ef7484fcc78603ede124e9e586 import EgtpServerOptions
        if self._properties.get('EgtpServerOptions', None) is None:
            return EgtpServerOptions(self)
        else:
            return self._properties.get('EgtpServerOptions')

    @property
    def EgtpSgwOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.egtpsgwoptions_a815efe97f0053663dab2a194220b27f.EgtpSgwOptions): An instance of the EgtpSgwOptions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.egtpsgwoptions_a815efe97f0053663dab2a194220b27f import EgtpSgwOptions
        if self._properties.get('EgtpSgwOptions', None) is None:
            return EgtpSgwOptions(self)
        else:
            return self._properties.get('EgtpSgwOptions')

    @property
    def Ethernet(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.ethernet_9270cf428cd566d0179a6cc2d36c2c51.Ethernet): An instance of the Ethernet class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.ethernet_9270cf428cd566d0179a6cc2d36c2c51 import Ethernet
        if self._properties.get('Ethernet', None) is None:
            return Ethernet(self)
        else:
            return self._properties.get('Ethernet')

    @property
    def EthernetEndpoint(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.ethernetendpoint_d505a70c25c539a0f7f57c724fbbdc10.EthernetEndpoint): An instance of the EthernetEndpoint class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.ethernetendpoint_d505a70c25c539a0f7f57c724fbbdc10 import EthernetEndpoint
        if self._properties.get('EthernetEndpoint', None) is None:
            return EthernetEndpoint(self)
        else:
            return self._properties.get('EthernetEndpoint')

    @property
    def EthernetOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.ethernetoptions_e2afbb391332ae673b33d4fa99666abc.EthernetOptions): An instance of the EthernetOptions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.ethernetoptions_e2afbb391332ae673b33d4fa99666abc import EthernetOptions
        if self._properties.get('EthernetOptions', None) is None:
            return EthernetOptions(self)
        else:
            return self._properties.get('EthernetOptions')

    @property
    def FcClientEndpoint(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.fcclientendpoint_7e5e9b26d670e7a4f77b28623de3f69a.FcClientEndpoint): An instance of the FcClientEndpoint class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.fcclientendpoint_7e5e9b26d670e7a4f77b28623de3f69a import FcClientEndpoint
        if self._properties.get('FcClientEndpoint', None) is None:
            return FcClientEndpoint(self)
        else:
            return self._properties.get('FcClientEndpoint')

    @property
    def FcClientOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.fcclientoptions_2888c6e9e7f909b50d27f503bbdee6af.FcClientOptions): An instance of the FcClientOptions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.fcclientoptions_2888c6e9e7f909b50d27f503bbdee6af import FcClientOptions
        if self._properties.get('FcClientOptions', None) is None:
            return FcClientOptions(self)
        else:
            return self._properties.get('FcClientOptions')

    @property
    def FcFportFwdEndpoint(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.fcfportfwdendpoint_f28ea5fd1bf83950a4aadd0d7a886489.FcFportFwdEndpoint): An instance of the FcFportFwdEndpoint class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.fcfportfwdendpoint_f28ea5fd1bf83950a4aadd0d7a886489 import FcFportFwdEndpoint
        if self._properties.get('FcFportFwdEndpoint', None) is None:
            return FcFportFwdEndpoint(self)
        else:
            return self._properties.get('FcFportFwdEndpoint')

    @property
    def FcFportOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.fcfportoptions_b1c1714bd27605ce452575322dc2d18e.FcFportOptions): An instance of the FcFportOptions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.fcfportoptions_b1c1714bd27605ce452575322dc2d18e import FcFportOptions
        if self._properties.get('FcFportOptions', None) is None:
            return FcFportOptions(self)
        else:
            return self._properties.get('FcFportOptions')

    @property
    def FcoeClientOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.fcoeclientoptions_38e2c7ce6db993624d36fe2016760c4c.FcoeClientOptions): An instance of the FcoeClientOptions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.fcoeclientoptions_38e2c7ce6db993624d36fe2016760c4c import FcoeClientOptions
        if self._properties.get('FcoeClientOptions', None) is None:
            return FcoeClientOptions(self)
        else:
            return self._properties.get('FcoeClientOptions')

    @property
    def FcoeFwdOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.fcoefwdoptions_c1ebfa7451c0fd226b21ca6a670f698a.FcoeFwdOptions): An instance of the FcoeFwdOptions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.fcoefwdoptions_c1ebfa7451c0fd226b21ca6a670f698a import FcoeFwdOptions
        if self._properties.get('FcoeFwdOptions', None) is None:
            return FcoeFwdOptions(self)
        else:
            return self._properties.get('FcoeFwdOptions')

    @property
    def IgmpOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.igmpoptions_af97dc2d88fdcb59ef3bcbc0c5ee0383.IgmpOptions): An instance of the IgmpOptions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.igmpoptions_af97dc2d88fdcb59ef3bcbc0c5ee0383 import IgmpOptions
        if self._properties.get('IgmpOptions', None) is None:
            return IgmpOptions(self)
        else:
            return self._properties.get('IgmpOptions')

    @property
    def IpRangeOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.iprangeoptions_e4c02903f7662a5dbdcd1ee5fc01c49d.IpRangeOptions): An instance of the IpRangeOptions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.iprangeoptions_e4c02903f7662a5dbdcd1ee5fc01c49d import IpRangeOptions
        if self._properties.get('IpRangeOptions', None) is None:
            return IpRangeOptions(self)
        else:
            return self._properties.get('IpRangeOptions')

    @property
    def L2tpOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.l2tpoptions_6924c5a1bebdbcd90ceed331b2bf3fa8.L2tpOptions): An instance of the L2tpOptions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.l2tpoptions_6924c5a1bebdbcd90ceed331b2bf3fa8 import L2tpOptions
        if self._properties.get('L2tpOptions', None) is None:
            return L2tpOptions(self)
        else:
            return self._properties.get('L2tpOptions')

    @property
    def Options(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.options_7469b94cd33b4b06719f0dd4ecfb6f8b.Options): An instance of the Options class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.options_7469b94cd33b4b06719f0dd4ecfb6f8b import Options
        if self._properties.get('Options', None) is None:
            return Options(self)._select()
        else:
            return self._properties.get('Options')

    @property
    def PppoxOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.pppoxoptions_f7eed5ece8c8b093f410f4b19e5321ba.PppoxOptions): An instance of the PppoxOptions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.pppoxoptions_f7eed5ece8c8b093f410f4b19e5321ba import PppoxOptions
        if self._properties.get('PppoxOptions', None) is None:
            return PppoxOptions(self)
        else:
            return self._properties.get('PppoxOptions')

    @property
    def PtpOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.ptpoptions_016c148d29be122b4ff63935e1a40089.PtpOptions): An instance of the PtpOptions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.ptpoptions_016c148d29be122b4ff63935e1a40089 import PtpOptions
        if self._properties.get('PtpOptions', None) is None:
            return PtpOptions(self)
        else:
            return self._properties.get('PtpOptions')

    @property
    def SmDnsOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.smdnsoptions_653d7eba98b73b1fad589c57df4e06db.SmDnsOptions): An instance of the SmDnsOptions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.smdnsoptions_653d7eba98b73b1fad589c57df4e06db import SmDnsOptions
        if self._properties.get('SmDnsOptions', None) is None:
            return SmDnsOptions(self)
        else:
            return self._properties.get('SmDnsOptions')

    @property
    def StaticHostsOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.statichostsoptions_b856e92d38cfb4c7f8e76ffd5c970154.StaticHostsOptions): An instance of the StaticHostsOptions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.statichostsoptions_b856e92d38cfb4c7f8e76ffd5c970154 import StaticHostsOptions
        if self._properties.get('StaticHostsOptions', None) is None:
            return StaticHostsOptions(self)
        else:
            return self._properties.get('StaticHostsOptions')

    @property
    def TwampOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.twampoptions_76cd16af4e6a3457023c413b90dc09b1.TwampOptions): An instance of the TwampOptions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.twampoptions_76cd16af4e6a3457023c413b90dc09b1 import TwampOptions
        if self._properties.get('TwampOptions', None) is None:
            return TwampOptions(self)
        else:
            return self._properties.get('TwampOptions')

    @property
    def TwampServerOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.twampserveroptions_d9df2e536efe64ac2a79662f006efe5c.TwampServerOptions): An instance of the TwampServerOptions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.twampserveroptions_d9df2e536efe64ac2a79662f006efe5c import TwampServerOptions
        if self._properties.get('TwampServerOptions', None) is None:
            return TwampServerOptions(self)
        else:
            return self._properties.get('TwampServerOptions')

    @property
    def VepaOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.vepaoptions_61de8697309d02e26cfdcfe37470fa44.VepaOptions): An instance of the VepaOptions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.vepaoptions_61de8697309d02e26cfdcfe37470fa44 import VepaOptions
        if self._properties.get('VepaOptions', None) is None:
            return VepaOptions(self)
        else:
            return self._properties.get('VepaOptions')

    @property
    def WebAuthOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.webauthoptions_53051bd801054f33723505dcef43b2b7.WebAuthOptions): An instance of the WebAuthOptions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.webauthoptions_53051bd801054f33723505dcef43b2b7 import WebAuthOptions
        if self._properties.get('WebAuthOptions', None) is None:
            return WebAuthOptions(self)
        else:
            return self._properties.get('WebAuthOptions')

    @property
    def ObjectId(self):
        """
        Returns
        -------
        - str: Unique identifier for this object
        """
        return self._get_attribute(self._SDM_ATT_MAP['ObjectId'])

    def CustomProtocolStack(self, *args, **kwargs):
        """Executes the customProtocolStack operation on the server.

        Create custom protocol stack under /vport/protocolStack

        customProtocolStack(Arg2=list, Arg3=enum)
        -----------------------------------------
        - Arg2 (list(str)): List of plugin types to be added in the new custom stack
        - Arg3 (str(kAppend | kMerge | kOverwrite)): Append, merge or overwrite existing protocol stack

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('customProtocolStack', payload=payload, response_object=None)

    def DisableProtocolStack(self, *args, **kwargs):
        """Executes the disableProtocolStack operation on the server.

        Disable a protocol under protocolStack using the class name

        disableProtocolStack(Arg2=string)string
        ---------------------------------------
        - Arg2 (str): Protocol class name to disable
        - Returns str: Status of the exec

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('disableProtocolStack', payload=payload, response_object=None)

    def EnableProtocolStack(self, *args, **kwargs):
        """Executes the enableProtocolStack operation on the server.

        Enable a protocol under protocolStack using the class name

        enableProtocolStack(Arg2=string)string
        --------------------------------------
        - Arg2 (str): Protocol class name to enable
        - Returns str: Status of the exec

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('enableProtocolStack', payload=payload, response_object=None)
