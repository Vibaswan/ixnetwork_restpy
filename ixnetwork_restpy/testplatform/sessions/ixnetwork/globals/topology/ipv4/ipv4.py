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


class Ipv4(Base):
    """IPv4 global and per-port settings
    The Ipv4 class encapsulates a required ipv4 resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'ipv4'

    def __init__(self, parent):
        super(Ipv4, self).__init__(parent)

    @property
    def ArpRate(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.ipv4.arprate.arprate.ArpRate): An instance of the ArpRate class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.ipv4.arprate.arprate import ArpRate
        return ArpRate(self)._select()

    @property
    def StartRate(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.ipv4.startrate.startrate.StartRate): An instance of the StartRate class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.ipv4.startrate.startrate import StartRate
        return StartRate(self)._select()

    @property
    def StopRate(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.ipv4.stoprate.stoprate.StopRate): An instance of the StopRate class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.ipv4.stoprate.stoprate import StopRate
        return StopRate(self)._select()

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
    def GratarpTransmitCount(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Number of times GRATARP packet is sent per source IPv4 address.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('gratarpTransmitCount'))

    @property
    def GratarpTransmitInterval(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Time interval to calculate next GRATARP packet transmission for each source IPv4 address.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('gratarpTransmitInterval'))

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
    def PermanentMacForGateway(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): When enabled, adds permanent entries for Gateways with manual MAC.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('permanentMacForGateway'))

    @property
    def RarpTransmitCount(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Number of times RARP packet is sent per source IPv4 address.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('rarpTransmitCount'))

    @property
    def RarpTransmitInterval(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Time interval to calculate next RARP packet transmission for each source IPv4 address.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('rarpTransmitInterval'))

    @property
    def ReSendArpOnLinkUp(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Resends ARP after link up.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('reSendArpOnLinkUp'))

    @property
    def RowNames(self):
        """
        Returns
        -------
        - list(str): Name of rows
        """
        return self._get_attribute('rowNames')

    @property
    def SuppressArpForDuplicateGateway(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Optimizes the gateway MAC discovery by sending a single ARP request for each unique destination.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('suppressArpForDuplicateGateway'))

    def update(self, Name=None):
        """Updates ipv4 resource on the server.

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

    def get_device_ids(self, PortNames=None, GratarpTransmitCount=None, GratarpTransmitInterval=None, PermanentMacForGateway=None, RarpTransmitCount=None, RarpTransmitInterval=None, ReSendArpOnLinkUp=None, SuppressArpForDuplicateGateway=None):
        """Base class infrastructure that gets a list of ipv4 device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - GratarpTransmitCount (str): optional regex of gratarpTransmitCount
        - GratarpTransmitInterval (str): optional regex of gratarpTransmitInterval
        - PermanentMacForGateway (str): optional regex of permanentMacForGateway
        - RarpTransmitCount (str): optional regex of rarpTransmitCount
        - RarpTransmitInterval (str): optional regex of rarpTransmitInterval
        - ReSendArpOnLinkUp (str): optional regex of reSendArpOnLinkUp
        - SuppressArpForDuplicateGateway (str): optional regex of suppressArpForDuplicateGateway

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
