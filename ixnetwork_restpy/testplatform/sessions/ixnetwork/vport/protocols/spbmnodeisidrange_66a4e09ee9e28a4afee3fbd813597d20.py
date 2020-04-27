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


class SpbmNodeIsIdRange(Base):
    """The SPBM Node ISIS ID Range.
    The SpbmNodeIsIdRange class encapsulates a list of spbmNodeIsIdRange resources that are managed by the user.
    A list of resources can be retrieved from the server using the SpbmNodeIsIdRange.find() method.
    The list can be managed by using the SpbmNodeIsIdRange.add() and SpbmNodeIsIdRange.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'spbmNodeIsIdRange'

    def __init__(self, parent):
        super(SpbmNodeIsIdRange, self).__init__(parent)

    @property
    def CMacAddressCount(self):
        """
        Returns
        -------
        - number: The number of C-MAC addresses.
        """
        return self._get_attribute('cMacAddressCount')
    @CMacAddressCount.setter
    def CMacAddressCount(self, value):
        self._set_attribute('cMacAddressCount', value)

    @property
    def CMacAddressStep(self):
        """
        Returns
        -------
        - str: The incremental value of C-MAC address.
        """
        return self._get_attribute('cMacAddressStep')
    @CMacAddressStep.setter
    def CMacAddressStep(self, value):
        self._set_attribute('cMacAddressStep', value)

    @property
    def ITagEthernetType(self):
        """
        Returns
        -------
        - number: The I-Tag Ethernet type. An I-Tag is a multiplexing tag for service instance scaling in Provider Bridged Networks.
        """
        return self._get_attribute('iTagEthernetType')

    @property
    def InterNodeCmacAddress(self):
        """
        Returns
        -------
        - str: The incremental value of the Inter Node C-MAC address.
        """
        return self._get_attribute('interNodeCmacAddress')
    @InterNodeCmacAddress.setter
    def InterNodeCmacAddress(self, value):
        self._set_attribute('interNodeCmacAddress', value)

    @property
    def InterNodeCvlan(self):
        """
        Returns
        -------
        - number: The Inter Node Stacked VLAN.
        """
        return self._get_attribute('interNodeCvlan')
    @InterNodeCvlan.setter
    def InterNodeCvlan(self, value):
        self._set_attribute('interNodeCvlan', value)

    @property
    def InterNodeIsIdIncrement(self):
        """
        Returns
        -------
        - number: The incremental value of Inter Node service identifier.
        """
        return self._get_attribute('interNodeIsIdIncrement')
    @InterNodeIsIdIncrement.setter
    def InterNodeIsIdIncrement(self, value):
        self._set_attribute('interNodeIsIdIncrement', value)

    @property
    def InterNodeSvlan(self):
        """
        Returns
        -------
        - number: The Inter Node Single VLAN.
        """
        return self._get_attribute('interNodeSvlan')
    @InterNodeSvlan.setter
    def InterNodeSvlan(self, value):
        self._set_attribute('interNodeSvlan', value)

    @property
    def IsId(self):
        """
        Returns
        -------
        - number: The I-component service identifier. The maximum value is 16777215. The minimum value is 0.
        """
        return self._get_attribute('isId')
    @IsId.setter
    def IsId(self, value):
        self._set_attribute('isId', value)

    @property
    def RBit(self):
        """
        Returns
        -------
        - bool: The Restart State bit.
        """
        return self._get_attribute('rBit')
    @RBit.setter
    def RBit(self, value):
        self._set_attribute('rBit', value)

    @property
    def StartCmacAddress(self):
        """
        Returns
        -------
        - str: The starting C-MAC address.
        """
        return self._get_attribute('startCmacAddress')
    @StartCmacAddress.setter
    def StartCmacAddress(self, value):
        self._set_attribute('startCmacAddress', value)

    @property
    def StartCvlan(self):
        """
        Returns
        -------
        - number: The starting value of Stacked VLAN.
        """
        return self._get_attribute('startCvlan')
    @StartCvlan.setter
    def StartCvlan(self, value):
        self._set_attribute('startCvlan', value)

    @property
    def StartSvlan(self):
        """
        Returns
        -------
        - number: The starting value of Single VLAN.
        """
        return self._get_attribute('startSvlan')
    @StartSvlan.setter
    def StartSvlan(self, value):
        self._set_attribute('startSvlan', value)

    @property
    def TBit(self):
        """
        Returns
        -------
        - bool: The external route tag bit.
        """
        return self._get_attribute('tBit')
    @TBit.setter
    def TBit(self, value):
        self._set_attribute('tBit', value)

    @property
    def TrafficDestMacAddress(self):
        """
        Returns
        -------
        - str: The traffic-destination MAC address.
        """
        return self._get_attribute('trafficDestMacAddress')
    @TrafficDestMacAddress.setter
    def TrafficDestMacAddress(self, value):
        self._set_attribute('trafficDestMacAddress', value)

    @property
    def TransmissionType(self):
        """
        Returns
        -------
        - number: Select the type of packet transmission. Options include Unicast and Multicast.
        """
        return self._get_attribute('transmissionType')
    @TransmissionType.setter
    def TransmissionType(self, value):
        self._set_attribute('transmissionType', value)

    @property
    def VlanType(self):
        """
        Returns
        -------
        - number: The type of VLAN.
        """
        return self._get_attribute('vlanType')
    @VlanType.setter
    def VlanType(self, value):
        self._set_attribute('vlanType', value)

    def update(self, CMacAddressCount=None, CMacAddressStep=None, InterNodeCmacAddress=None, InterNodeCvlan=None, InterNodeIsIdIncrement=None, InterNodeSvlan=None, IsId=None, RBit=None, StartCmacAddress=None, StartCvlan=None, StartSvlan=None, TBit=None, TrafficDestMacAddress=None, TransmissionType=None, VlanType=None):
        """Updates spbmNodeIsIdRange resource on the server.

        Args
        ----
        - CMacAddressCount (number): The number of C-MAC addresses.
        - CMacAddressStep (str): The incremental value of C-MAC address.
        - InterNodeCmacAddress (str): The incremental value of the Inter Node C-MAC address.
        - InterNodeCvlan (number): The Inter Node Stacked VLAN.
        - InterNodeIsIdIncrement (number): The incremental value of Inter Node service identifier.
        - InterNodeSvlan (number): The Inter Node Single VLAN.
        - IsId (number): The I-component service identifier. The maximum value is 16777215. The minimum value is 0.
        - RBit (bool): The Restart State bit.
        - StartCmacAddress (str): The starting C-MAC address.
        - StartCvlan (number): The starting value of Stacked VLAN.
        - StartSvlan (number): The starting value of Single VLAN.
        - TBit (bool): The external route tag bit.
        - TrafficDestMacAddress (str): The traffic-destination MAC address.
        - TransmissionType (number): Select the type of packet transmission. Options include Unicast and Multicast.
        - VlanType (number): The type of VLAN.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(locals())

    def add(self, CMacAddressCount=None, CMacAddressStep=None, InterNodeCmacAddress=None, InterNodeCvlan=None, InterNodeIsIdIncrement=None, InterNodeSvlan=None, IsId=None, RBit=None, StartCmacAddress=None, StartCvlan=None, StartSvlan=None, TBit=None, TrafficDestMacAddress=None, TransmissionType=None, VlanType=None):
        """Adds a new spbmNodeIsIdRange resource on the server and adds it to the container.

        Args
        ----
        - CMacAddressCount (number): The number of C-MAC addresses.
        - CMacAddressStep (str): The incremental value of C-MAC address.
        - InterNodeCmacAddress (str): The incremental value of the Inter Node C-MAC address.
        - InterNodeCvlan (number): The Inter Node Stacked VLAN.
        - InterNodeIsIdIncrement (number): The incremental value of Inter Node service identifier.
        - InterNodeSvlan (number): The Inter Node Single VLAN.
        - IsId (number): The I-component service identifier. The maximum value is 16777215. The minimum value is 0.
        - RBit (bool): The Restart State bit.
        - StartCmacAddress (str): The starting C-MAC address.
        - StartCvlan (number): The starting value of Stacked VLAN.
        - StartSvlan (number): The starting value of Single VLAN.
        - TBit (bool): The external route tag bit.
        - TrafficDestMacAddress (str): The traffic-destination MAC address.
        - TransmissionType (number): Select the type of packet transmission. Options include Unicast and Multicast.
        - VlanType (number): The type of VLAN.

        Returns
        -------
        - self: This instance with all currently retrieved spbmNodeIsIdRange resources using find and the newly added spbmNodeIsIdRange resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(locals())

    def remove(self):
        """Deletes all the contained spbmNodeIsIdRange resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, CMacAddressCount=None, CMacAddressStep=None, ITagEthernetType=None, InterNodeCmacAddress=None, InterNodeCvlan=None, InterNodeIsIdIncrement=None, InterNodeSvlan=None, IsId=None, RBit=None, StartCmacAddress=None, StartCvlan=None, StartSvlan=None, TBit=None, TrafficDestMacAddress=None, TransmissionType=None, VlanType=None):
        """Finds and retrieves spbmNodeIsIdRange resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve spbmNodeIsIdRange resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all spbmNodeIsIdRange resources from the server.

        Args
        ----
        - CMacAddressCount (number): The number of C-MAC addresses.
        - CMacAddressStep (str): The incremental value of C-MAC address.
        - ITagEthernetType (number): The I-Tag Ethernet type. An I-Tag is a multiplexing tag for service instance scaling in Provider Bridged Networks.
        - InterNodeCmacAddress (str): The incremental value of the Inter Node C-MAC address.
        - InterNodeCvlan (number): The Inter Node Stacked VLAN.
        - InterNodeIsIdIncrement (number): The incremental value of Inter Node service identifier.
        - InterNodeSvlan (number): The Inter Node Single VLAN.
        - IsId (number): The I-component service identifier. The maximum value is 16777215. The minimum value is 0.
        - RBit (bool): The Restart State bit.
        - StartCmacAddress (str): The starting C-MAC address.
        - StartCvlan (number): The starting value of Stacked VLAN.
        - StartSvlan (number): The starting value of Single VLAN.
        - TBit (bool): The external route tag bit.
        - TrafficDestMacAddress (str): The traffic-destination MAC address.
        - TransmissionType (number): Select the type of packet transmission. Options include Unicast and Multicast.
        - VlanType (number): The type of VLAN.

        Returns
        -------
        - self: This instance with matching spbmNodeIsIdRange resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of spbmNodeIsIdRange data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the spbmNodeIsIdRange resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
