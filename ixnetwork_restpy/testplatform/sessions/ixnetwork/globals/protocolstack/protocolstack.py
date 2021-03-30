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
    """
    The ProtocolStack class encapsulates a required protocolStack resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'protocolStack'
    _SDM_ATT_MAP = {
    }

    def __init__(self, parent):
        super(ProtocolStack, self).__init__(parent)

    @property
    def AmtGlobals(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.amtglobals.amtglobals.AmtGlobals): An instance of the AmtGlobals class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.amtglobals.amtglobals import AmtGlobals
        if self._properties.get('AmtGlobals', None) is None:
            return AmtGlobals(self)
        else:
            return self._properties.get('AmtGlobals')

    @property
    def AncpGlobals(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.ancpglobals.ancpglobals.AncpGlobals): An instance of the AncpGlobals class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.ancpglobals.ancpglobals import AncpGlobals
        if self._properties.get('AncpGlobals', None) is None:
            return AncpGlobals(self)
        else:
            return self._properties.get('AncpGlobals')

    @property
    def DcbxGlobals(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.dcbxglobals.dcbxglobals.DcbxGlobals): An instance of the DcbxGlobals class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.dcbxglobals.dcbxglobals import DcbxGlobals
        if self._properties.get('DcbxGlobals', None) is None:
            return DcbxGlobals(self)
        else:
            return self._properties.get('DcbxGlobals')

    @property
    def DhcpGlobals(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.dhcpglobals.dhcpglobals.DhcpGlobals): An instance of the DhcpGlobals class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.dhcpglobals.dhcpglobals import DhcpGlobals
        if self._properties.get('DhcpGlobals', None) is None:
            return DhcpGlobals(self)
        else:
            return self._properties.get('DhcpGlobals')

    @property
    def DhcpHostsGlobals(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.dhcphostsglobals.dhcphostsglobals.DhcpHostsGlobals): An instance of the DhcpHostsGlobals class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.dhcphostsglobals.dhcphostsglobals import DhcpHostsGlobals
        if self._properties.get('DhcpHostsGlobals', None) is None:
            return DhcpHostsGlobals(self)
        else:
            return self._properties.get('DhcpHostsGlobals')

    @property
    def DhcpServerGlobals(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.dhcpserverglobals.dhcpserverglobals.DhcpServerGlobals): An instance of the DhcpServerGlobals class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.dhcpserverglobals.dhcpserverglobals import DhcpServerGlobals
        if self._properties.get('DhcpServerGlobals', None) is None:
            return DhcpServerGlobals(self)
        else:
            return self._properties.get('DhcpServerGlobals')

    @property
    def Dhcpv6ClientGlobals(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.dhcpv6clientglobals.dhcpv6clientglobals.Dhcpv6ClientGlobals): An instance of the Dhcpv6ClientGlobals class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.dhcpv6clientglobals.dhcpv6clientglobals import Dhcpv6ClientGlobals
        if self._properties.get('Dhcpv6ClientGlobals', None) is None:
            return Dhcpv6ClientGlobals(self)
        else:
            return self._properties.get('Dhcpv6ClientGlobals')

    @property
    def Dhcpv6PdClientGlobals(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.dhcpv6pdclientglobals.dhcpv6pdclientglobals.Dhcpv6PdClientGlobals): An instance of the Dhcpv6PdClientGlobals class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.dhcpv6pdclientglobals.dhcpv6pdclientglobals import Dhcpv6PdClientGlobals
        if self._properties.get('Dhcpv6PdClientGlobals', None) is None:
            return Dhcpv6PdClientGlobals(self)
        else:
            return self._properties.get('Dhcpv6PdClientGlobals')

    @property
    def Dhcpv6ServerGlobals(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.dhcpv6serverglobals.dhcpv6serverglobals.Dhcpv6ServerGlobals): An instance of the Dhcpv6ServerGlobals class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.dhcpv6serverglobals.dhcpv6serverglobals import Dhcpv6ServerGlobals
        if self._properties.get('Dhcpv6ServerGlobals', None) is None:
            return Dhcpv6ServerGlobals(self)
        else:
            return self._properties.get('Dhcpv6ServerGlobals')

    @property
    def Dot1xGlobals(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.dot1xglobals.dot1xglobals.Dot1xGlobals): An instance of the Dot1xGlobals class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.dot1xglobals.dot1xglobals import Dot1xGlobals
        if self._properties.get('Dot1xGlobals', None) is None:
            return Dot1xGlobals(self)
        else:
            return self._properties.get('Dot1xGlobals')

    @property
    def EapoUdpGlobals(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.eapoudpglobals.eapoudpglobals.EapoUdpGlobals): An instance of the EapoUdpGlobals class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.eapoudpglobals.eapoudpglobals import EapoUdpGlobals
        if self._properties.get('EapoUdpGlobals', None) is None:
            return EapoUdpGlobals(self)
        else:
            return self._properties.get('EapoUdpGlobals')

    @property
    def EgtpClientGlobals(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.egtpclientglobals.egtpclientglobals.EgtpClientGlobals): An instance of the EgtpClientGlobals class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.egtpclientglobals.egtpclientglobals import EgtpClientGlobals
        if self._properties.get('EgtpClientGlobals', None) is None:
            return EgtpClientGlobals(self)
        else:
            return self._properties.get('EgtpClientGlobals')

    @property
    def EgtpGlobalsBase(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.egtpglobalsbase.egtpglobalsbase.EgtpGlobalsBase): An instance of the EgtpGlobalsBase class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.egtpglobalsbase.egtpglobalsbase import EgtpGlobalsBase
        if self._properties.get('EgtpGlobalsBase', None) is None:
            return EgtpGlobalsBase(self)
        else:
            return self._properties.get('EgtpGlobalsBase')

    @property
    def EgtpS5S8PgwGlobals(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.egtps5s8pgwglobals.egtps5s8pgwglobals.EgtpS5S8PgwGlobals): An instance of the EgtpS5S8PgwGlobals class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.egtps5s8pgwglobals.egtps5s8pgwglobals import EgtpS5S8PgwGlobals
        if self._properties.get('EgtpS5S8PgwGlobals', None) is None:
            return EgtpS5S8PgwGlobals(self)
        else:
            return self._properties.get('EgtpS5S8PgwGlobals')

    @property
    def EgtpS5S8SgwGlobals(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.egtps5s8sgwglobals.egtps5s8sgwglobals.EgtpS5S8SgwGlobals): An instance of the EgtpS5S8SgwGlobals class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.egtps5s8sgwglobals.egtps5s8sgwglobals import EgtpS5S8SgwGlobals
        if self._properties.get('EgtpS5S8SgwGlobals', None) is None:
            return EgtpS5S8SgwGlobals(self)
        else:
            return self._properties.get('EgtpS5S8SgwGlobals')

    @property
    def EgtpSgwGlobals(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.egtpsgwglobals.egtpsgwglobals.EgtpSgwGlobals): An instance of the EgtpSgwGlobals class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.egtpsgwglobals.egtpsgwglobals import EgtpSgwGlobals
        if self._properties.get('EgtpSgwGlobals', None) is None:
            return EgtpSgwGlobals(self)
        else:
            return self._properties.get('EgtpSgwGlobals')

    @property
    def FcClientGlobals(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.fcclientglobals.fcclientglobals.FcClientGlobals): An instance of the FcClientGlobals class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.fcclientglobals.fcclientglobals import FcClientGlobals
        if self._properties.get('FcClientGlobals', None) is None:
            return FcClientGlobals(self)
        else:
            return self._properties.get('FcClientGlobals')

    @property
    def FcFportGlobals(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.fcfportglobals.fcfportglobals.FcFportGlobals): An instance of the FcFportGlobals class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.fcfportglobals.fcfportglobals import FcFportGlobals
        if self._properties.get('FcFportGlobals', None) is None:
            return FcFportGlobals(self)
        else:
            return self._properties.get('FcFportGlobals')

    @property
    def FcoeClientGlobals(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.fcoeclientglobals.fcoeclientglobals.FcoeClientGlobals): An instance of the FcoeClientGlobals class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.fcoeclientglobals.fcoeclientglobals import FcoeClientGlobals
        if self._properties.get('FcoeClientGlobals', None) is None:
            return FcoeClientGlobals(self)
        else:
            return self._properties.get('FcoeClientGlobals')

    @property
    def FcoeFwdGlobals(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.fcoefwdglobals.fcoefwdglobals.FcoeFwdGlobals): An instance of the FcoeFwdGlobals class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.fcoefwdglobals.fcoefwdglobals import FcoeFwdGlobals
        if self._properties.get('FcoeFwdGlobals', None) is None:
            return FcoeFwdGlobals(self)
        else:
            return self._properties.get('FcoeFwdGlobals')

    @property
    def IgmpGlobals(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.igmpglobals.igmpglobals.IgmpGlobals): An instance of the IgmpGlobals class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.igmpglobals.igmpglobals import IgmpGlobals
        if self._properties.get('IgmpGlobals', None) is None:
            return IgmpGlobals(self)
        else:
            return self._properties.get('IgmpGlobals')

    @property
    def IpGlobals(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.ipglobals.ipglobals.IpGlobals): An instance of the IpGlobals class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.ipglobals.ipglobals import IpGlobals
        if self._properties.get('IpGlobals', None) is None:
            return IpGlobals(self)
        else:
            return self._properties.get('IpGlobals')

    @property
    def IptvGlobals(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.iptvglobals.iptvglobals.IptvGlobals): An instance of the IptvGlobals class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.iptvglobals.iptvglobals import IptvGlobals
        if self._properties.get('IptvGlobals', None) is None:
            return IptvGlobals(self)
        else:
            return self._properties.get('IptvGlobals')

    @property
    def L2tpGlobals(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.l2tpglobals.l2tpglobals.L2tpGlobals): An instance of the L2tpGlobals class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.l2tpglobals.l2tpglobals import L2tpGlobals
        if self._properties.get('L2tpGlobals', None) is None:
            return L2tpGlobals(self)
        else:
            return self._properties.get('L2tpGlobals')

    @property
    def PppoxGlobals(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.pppoxglobals.pppoxglobals.PppoxGlobals): An instance of the PppoxGlobals class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.pppoxglobals.pppoxglobals import PppoxGlobals
        if self._properties.get('PppoxGlobals', None) is None:
            return PppoxGlobals(self)
        else:
            return self._properties.get('PppoxGlobals')

    @property
    def PtpGlobals(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.ptpglobals.ptpglobals.PtpGlobals): An instance of the PtpGlobals class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.ptpglobals.ptpglobals import PtpGlobals
        if self._properties.get('PtpGlobals', None) is None:
            return PtpGlobals(self)
        else:
            return self._properties.get('PtpGlobals')

    @property
    def RadiusGlobals(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.radiusglobals.radiusglobals.RadiusGlobals): An instance of the RadiusGlobals class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.radiusglobals.radiusglobals import RadiusGlobals
        if self._properties.get('RadiusGlobals', None) is None:
            return RadiusGlobals(self)
        else:
            return self._properties.get('RadiusGlobals')

    @property
    def StaticHostsGlobals(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.statichostsglobals.statichostsglobals.StaticHostsGlobals): An instance of the StaticHostsGlobals class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.statichostsglobals.statichostsglobals import StaticHostsGlobals
        if self._properties.get('StaticHostsGlobals', None) is None:
            return StaticHostsGlobals(self)
        else:
            return self._properties.get('StaticHostsGlobals')

    @property
    def TwampGlobals(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.twampglobals.twampglobals.TwampGlobals): An instance of the TwampGlobals class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.twampglobals.twampglobals import TwampGlobals
        if self._properties.get('TwampGlobals', None) is None:
            return TwampGlobals(self)
        else:
            return self._properties.get('TwampGlobals')

    @property
    def VepaGlobals(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.vepaglobals.vepaglobals.VepaGlobals): An instance of the VepaGlobals class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.vepaglobals.vepaglobals import VepaGlobals
        if self._properties.get('VepaGlobals', None) is None:
            return VepaGlobals(self)
        else:
            return self._properties.get('VepaGlobals')

    @property
    def VicClientGlobals(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.vicclientglobals.vicclientglobals.VicClientGlobals): An instance of the VicClientGlobals class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.vicclientglobals.vicclientglobals import VicClientGlobals
        if self._properties.get('VicClientGlobals', None) is None:
            return VicClientGlobals(self)
        else:
            return self._properties.get('VicClientGlobals')

    @property
    def WebAuthGlobals(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.webauthglobals.webauthglobals.WebAuthGlobals): An instance of the WebAuthGlobals class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.webauthglobals.webauthglobals import WebAuthGlobals
        if self._properties.get('WebAuthGlobals', None) is None:
            return WebAuthGlobals(self)
        else:
            return self._properties.get('WebAuthGlobals')
