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


class Ipv4Multicast(Base):
    """The DCE ISIS Learned Information option fetches the learned information for the IPv4 Multicast Range of a particular DCE ISIS router.
    The Ipv4Multicast class encapsulates a list of ipv4Multicast resources that are managed by the system.
    A list of resources can be retrieved from the server using the Ipv4Multicast.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'ipv4Multicast'
    _SDM_ATT_MAP = {
        'Age': 'age',
        'HostName': 'hostName',
        'Ipv4MulticastGroupAddress': 'ipv4MulticastGroupAddress',
        'LspId': 'lspId',
        'SequenceNumber': 'sequenceNumber',
        'VlanId': 'vlanId',
    }

    def __init__(self, parent):
        super(Ipv4Multicast, self).__init__(parent)

    @property
    def Ipv4UnicastItem(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv4unicastitem_f1998a7e7e04e8d70a80686a3036fc31.Ipv4UnicastItem): An instance of the Ipv4UnicastItem class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ipv4unicastitem_f1998a7e7e04e8d70a80686a3036fc31 import Ipv4UnicastItem
        if self._properties.get('Ipv4UnicastItem', None) is None:
            return Ipv4UnicastItem(self)
        else:
            return self._properties.get('Ipv4UnicastItem')

    @property
    def Age(self):
        """
        Returns
        -------
        - number: This indicates the age in time, in seconds, since it was last refreshed.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Age'])

    @property
    def HostName(self):
        """
        Returns
        -------
        - str: The host name as retrieved from the related packets.
        """
        return self._get_attribute(self._SDM_ATT_MAP['HostName'])

    @property
    def Ipv4MulticastGroupAddress(self):
        """
        Returns
        -------
        - str: This indicates the IPv4 Multicast Group Address in the Group Record.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv4MulticastGroupAddress'])

    @property
    def LspId(self):
        """
        Returns
        -------
        - str: This indicates the LSP identification number.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LspId'])

    @property
    def SequenceNumber(self):
        """
        Returns
        -------
        - number: This indicates the sequence number of the LSP containing the route.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SequenceNumber'])

    @property
    def VlanId(self):
        """
        Returns
        -------
        - number: This indicates the VLAN ID in the Group Record.
        """
        return self._get_attribute(self._SDM_ATT_MAP['VlanId'])

    def find(self, Age=None, HostName=None, Ipv4MulticastGroupAddress=None, LspId=None, SequenceNumber=None, VlanId=None):
        """Finds and retrieves ipv4Multicast resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve ipv4Multicast resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all ipv4Multicast resources from the server.

        Args
        ----
        - Age (number): This indicates the age in time, in seconds, since it was last refreshed.
        - HostName (str): The host name as retrieved from the related packets.
        - Ipv4MulticastGroupAddress (str): This indicates the IPv4 Multicast Group Address in the Group Record.
        - LspId (str): This indicates the LSP identification number.
        - SequenceNumber (number): This indicates the sequence number of the LSP containing the route.
        - VlanId (number): This indicates the VLAN ID in the Group Record.

        Returns
        -------
        - self: This instance with matching ipv4Multicast resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of ipv4Multicast data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the ipv4Multicast resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
