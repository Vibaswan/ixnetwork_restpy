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


class VxlanIPv6StaticInfo(Base):
    """VXLANv6 Unicast Info
    The VxlanIPv6StaticInfo class encapsulates a required vxlanIPv6StaticInfo resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'vxlanIPv6StaticInfo'

    def __init__(self, parent):
        super(VxlanIPv6StaticInfo, self).__init__(parent)

    @property
    def Active(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Flag.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('active'))

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
    def EnableManualRemoteVMMac(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Statically configure the Remote Inner Mac address to Outer Vtep IPv6 mapping, used for traffic.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('enableManualRemoteVMMac'))

    @property
    def LocalVNI(self):
        """
        Returns
        -------
        - list(str): VNI
        """
        return self._get_attribute('localVNI')

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
    def RemoteVMIpv4(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): VM IPv4 Address.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('remoteVMIpv4'))

    @property
    def RemoteVMMacAddress(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Remote VM MAC address
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('remoteVMMacAddress'))

    @property
    def RemoteVtepUnicastIpv6(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Remote VTEP Unicast IPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('remoteVtepUnicastIpv6'))

    @property
    def SuppressArp(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Suppress Arp for VM IP, VM MAC pair.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('suppressArp'))

    def update(self, Name=None):
        """Updates vxlanIPv6StaticInfo resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(locals())

    def get_device_ids(self, PortNames=None, Active=None, EnableManualRemoteVMMac=None, RemoteVMIpv4=None, RemoteVMMacAddress=None, RemoteVtepUnicastIpv6=None, SuppressArp=None):
        """Base class infrastructure that gets a list of vxlanIPv6StaticInfo device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active
        - EnableManualRemoteVMMac (str): optional regex of enableManualRemoteVMMac
        - RemoteVMIpv4 (str): optional regex of remoteVMIpv4
        - RemoteVMMacAddress (str): optional regex of remoteVMMacAddress
        - RemoteVtepUnicastIpv6 (str): optional regex of remoteVtepUnicastIpv6
        - SuppressArp (str): optional regex of suppressArp

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
