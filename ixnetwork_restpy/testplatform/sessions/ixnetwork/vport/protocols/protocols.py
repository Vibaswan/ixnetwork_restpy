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


class Protocols(Base):
    """Allows the user to select a set of protocols that are enabled for a newly added port.
    The Protocols class encapsulates a list of protocols resources that are managed by the system.
    A list of resources can be retrieved from the server using the Protocols.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'protocols'
    _SDM_ATT_MAP = {
        'ProtocolMaxNodeCount': 'protocolMaxNodeCount',
    }

    def __init__(self, parent):
        super(Protocols, self).__init__(parent)

    @property
    def Arp(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.arp_02ad3a87af613c0238e23157d241afd5.Arp): An instance of the Arp class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.arp_02ad3a87af613c0238e23157d241afd5 import Arp
        if self._properties.get('Arp', None) is None:
            return Arp(self)
        else:
            return self._properties.get('Arp')

    @property
    def Bfd(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.bfd_d5e88ec401a1941c80be1a5a01aa0e3b.Bfd): An instance of the Bfd class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.bfd_d5e88ec401a1941c80be1a5a01aa0e3b import Bfd
        if self._properties.get('Bfd', None) is None:
            return Bfd(self)._select()
        else:
            return self._properties.get('Bfd')

    @property
    def Bgp(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.bgp_eaa18e059aea3db7489e5e5975c78393.Bgp): An instance of the Bgp class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.bgp_eaa18e059aea3db7489e5e5975c78393 import Bgp
        if self._properties.get('Bgp', None) is None:
            return Bgp(self)._select()
        else:
            return self._properties.get('Bgp')

    @property
    def Cfm(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.cfm_a96182d068c89cc1a09d61bc9826454e.Cfm): An instance of the Cfm class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.cfm_a96182d068c89cc1a09d61bc9826454e import Cfm
        if self._properties.get('Cfm', None) is None:
            return Cfm(self)._select()
        else:
            return self._properties.get('Cfm')

    @property
    def Eigrp(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.eigrp_8c0911879bb0fc33556819b581ef1cd5.Eigrp): An instance of the Eigrp class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.eigrp_8c0911879bb0fc33556819b581ef1cd5 import Eigrp
        if self._properties.get('Eigrp', None) is None:
            return Eigrp(self)._select()
        else:
            return self._properties.get('Eigrp')

    @property
    def Elmi(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.elmi_e04c43a1f4f61fd0c7e21feec7754432.Elmi): An instance of the Elmi class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.elmi_e04c43a1f4f61fd0c7e21feec7754432 import Elmi
        if self._properties.get('Elmi', None) is None:
            return Elmi(self)._select()
        else:
            return self._properties.get('Elmi')

    @property
    def Igmp(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.igmp_9e398aa1578ce37d86fcb3bff949b26a.Igmp): An instance of the Igmp class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.igmp_9e398aa1578ce37d86fcb3bff949b26a import Igmp
        if self._properties.get('Igmp', None) is None:
            return Igmp(self)._select()
        else:
            return self._properties.get('Igmp')

    @property
    def Isis(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.isis_ed275f3afdd4b191a3a0bf3a3e4fcf23.Isis): An instance of the Isis class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.isis_ed275f3afdd4b191a3a0bf3a3e4fcf23 import Isis
        if self._properties.get('Isis', None) is None:
            return Isis(self)._select()
        else:
            return self._properties.get('Isis')

    @property
    def Lacp(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.lacp_c536b7fd522e328f25d1b7294149d8d5.Lacp): An instance of the Lacp class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.lacp_c536b7fd522e328f25d1b7294149d8d5 import Lacp
        if self._properties.get('Lacp', None) is None:
            return Lacp(self)._select()
        else:
            return self._properties.get('Lacp')

    @property
    def Ldp(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ldp_896c0d96a713502abc9340d8047a5f9d.Ldp): An instance of the Ldp class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ldp_896c0d96a713502abc9340d8047a5f9d import Ldp
        if self._properties.get('Ldp', None) is None:
            return Ldp(self)._select()
        else:
            return self._properties.get('Ldp')

    @property
    def LinkOam(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.linkoam_5924c549b7c15a4bb415f30f997378d2.LinkOam): An instance of the LinkOam class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.linkoam_5924c549b7c15a4bb415f30f997378d2 import LinkOam
        if self._properties.get('LinkOam', None) is None:
            return LinkOam(self)._select()
        else:
            return self._properties.get('LinkOam')

    @property
    def Lisp(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.lisp_7412d0bff0b602ec68ba446d28f90626.Lisp): An instance of the Lisp class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.lisp_7412d0bff0b602ec68ba446d28f90626 import Lisp
        if self._properties.get('Lisp', None) is None:
            return Lisp(self)._select()
        else:
            return self._properties.get('Lisp')

    @property
    def Mld(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.mld_f1161f34d4a4d525e0d1c8288951f7e6.Mld): An instance of the Mld class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.mld_f1161f34d4a4d525e0d1c8288951f7e6 import Mld
        if self._properties.get('Mld', None) is None:
            return Mld(self)._select()
        else:
            return self._properties.get('Mld')

    @property
    def MplsOam(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.mplsoam_c5ec6f5217261009d57292d968097bd8.MplsOam): An instance of the MplsOam class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.mplsoam_c5ec6f5217261009d57292d968097bd8 import MplsOam
        if self._properties.get('MplsOam', None) is None:
            return MplsOam(self)._select()
        else:
            return self._properties.get('MplsOam')

    @property
    def MplsTp(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.mplstp_77f517ba5758139a40ffca4f733d6d7d.MplsTp): An instance of the MplsTp class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.mplstp_77f517ba5758139a40ffca4f733d6d7d import MplsTp
        if self._properties.get('MplsTp', None) is None:
            return MplsTp(self)._select()
        else:
            return self._properties.get('MplsTp')

    @property
    def OpenFlow(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.openflow_ade3a58bbdcdf92d5bc0db71ff6aa555.OpenFlow): An instance of the OpenFlow class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.openflow_ade3a58bbdcdf92d5bc0db71ff6aa555 import OpenFlow
        if self._properties.get('OpenFlow', None) is None:
            return OpenFlow(self)._select()
        else:
            return self._properties.get('OpenFlow')

    @property
    def Ospf(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ospf_ececb387932f5a00700a5d4ee1d36de9.Ospf): An instance of the Ospf class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ospf_ececb387932f5a00700a5d4ee1d36de9 import Ospf
        if self._properties.get('Ospf', None) is None:
            return Ospf(self)._select()
        else:
            return self._properties.get('Ospf')

    @property
    def OspfV3(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ospfv3_34232cdb18da44847a8884d00dc4b2ba.OspfV3): An instance of the OspfV3 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ospfv3_34232cdb18da44847a8884d00dc4b2ba import OspfV3
        if self._properties.get('OspfV3', None) is None:
            return OspfV3(self)._select()
        else:
            return self._properties.get('OspfV3')

    @property
    def Pimsm(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.pimsm_33ba141f2aa1f04e67b06fb3580eec0d.Pimsm): An instance of the Pimsm class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.pimsm_33ba141f2aa1f04e67b06fb3580eec0d import Pimsm
        if self._properties.get('Pimsm', None) is None:
            return Pimsm(self)._select()
        else:
            return self._properties.get('Pimsm')

    @property
    def Ping(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ping_0ede3677595a61e44be090b8970ef408.Ping): An instance of the Ping class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ping_0ede3677595a61e44be090b8970ef408 import Ping
        if self._properties.get('Ping', None) is None:
            return Ping(self)
        else:
            return self._properties.get('Ping')

    @property
    def Rip(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.rip_ad63955be154e2f3b80204b8ae6114dc.Rip): An instance of the Rip class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.rip_ad63955be154e2f3b80204b8ae6114dc import Rip
        if self._properties.get('Rip', None) is None:
            return Rip(self)._select()
        else:
            return self._properties.get('Rip')

    @property
    def Ripng(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ripng_cf5e0e826b2079e4dfc76d9c1ce9f4e8.Ripng): An instance of the Ripng class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ripng_cf5e0e826b2079e4dfc76d9c1ce9f4e8 import Ripng
        if self._properties.get('Ripng', None) is None:
            return Ripng(self)._select()
        else:
            return self._properties.get('Ripng')

    @property
    def Rsvp(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.rsvp_94f31353a0f6b62a8a1920dfb1c87e99.Rsvp): An instance of the Rsvp class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.rsvp_94f31353a0f6b62a8a1920dfb1c87e99 import Rsvp
        if self._properties.get('Rsvp', None) is None:
            return Rsvp(self)._select()
        else:
            return self._properties.get('Rsvp')

    @property
    def Static(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.static_6aeb02f98d8f1810c1a06cf568987348.Static): An instance of the Static class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.static_6aeb02f98d8f1810c1a06cf568987348 import Static
        if self._properties.get('Static', None) is None:
            return Static(self)._select()
        else:
            return self._properties.get('Static')

    @property
    def Stp(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.stp_4de133a97c1f0320b38f5c69c651d367.Stp): An instance of the Stp class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.stp_4de133a97c1f0320b38f5c69c651d367 import Stp
        if self._properties.get('Stp', None) is None:
            return Stp(self)._select()
        else:
            return self._properties.get('Stp')

    @property
    def ProtocolMaxNodeCount(self):
        """
        Returns
        -------
        - number: Shows maximum number of node.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ProtocolMaxNodeCount'])

    def find(self, ProtocolMaxNodeCount=None):
        """Finds and retrieves protocols resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve protocols resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all protocols resources from the server.

        Args
        ----
        - ProtocolMaxNodeCount (number): Shows maximum number of node.

        Returns
        -------
        - self: This instance with matching protocols resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of protocols data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the protocols resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
