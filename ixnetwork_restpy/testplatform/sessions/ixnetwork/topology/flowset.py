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


class FlowSet(Base):
    """Flow Set Configuration
    The FlowSet class encapsulates a list of flowSet resources that are managed by the system.
    A list of resources can be retrieved from the server using the FlowSet.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'flowSet'

    def __init__(self, parent):
        super(FlowSet, self).__init__(parent)

    @property
    def FlowProfile(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.flowprofile.FlowProfile): An instance of the FlowProfile class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.flowprofile import FlowProfile
        return FlowProfile(self)._select()

    @property
    def Active(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Activate/Deactivate Configuration
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('active'))

    @property
    def Cookie(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Cookie of the flow entry that was looked up. This is the opaque controller-issued identifier.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('cookie'))

    @property
    def CookieMask(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The mask used to restrict the cookie bits.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('cookieMask'))

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
    def FlowAdvertise(self):
        """
        Returns
        -------
        - bool: If selected, the flows are advertised by the OF Channel.
        """
        return self._get_attribute('flowAdvertise')
    @FlowAdvertise.setter
    def FlowAdvertise(self, value):
        self._set_attribute('flowAdvertise', value)

    @property
    def FlowFlags(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Allows to configure the Flow Flags. Options are: 1) Send Flow Removed 2) Check Overlap 3) Reset Counts 4) No Packet Count 5) No Byte Count
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('flowFlags'))

    @property
    def FlowMatchType(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The type of match to be configured. Options include the following: 1) Strict 2) Loose
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('flowMatchType'))

    @property
    def FlowSetId(self):
        """
        Returns
        -------
        - str: Specify the controller Flow Set identifier.
        """
        return self._get_attribute('flowSetId')
    @FlowSetId.setter
    def FlowSetId(self, value):
        self._set_attribute('flowSetId', value)

    @property
    def HardTimeout(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The inactive time in seconds after which the Flow range will hard timeout and close.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('hardTimeout'))

    @property
    def IdleTimeout(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The inactive time in seconds after which the Flow range will timeout and become idle.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('idleTimeout'))

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
    def NumberOfFlows(self):
        """
        Returns
        -------
        - number: The number of flows to be configured for the controller table.
        """
        return self._get_attribute('numberOfFlows')
    @NumberOfFlows.setter
    def NumberOfFlows(self, value):
        self._set_attribute('numberOfFlows', value)

    @property
    def Priority(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The priority level for the Flow Range.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('priority'))

    def update(self, FlowAdvertise=None, FlowSetId=None, Name=None, NumberOfFlows=None):
        """Updates flowSet resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - FlowAdvertise (bool): If selected, the flows are advertised by the OF Channel.
        - FlowSetId (str): Specify the controller Flow Set identifier.
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NumberOfFlows (number): The number of flows to be configured for the controller table.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(locals())

    def find(self, Count=None, DescriptiveName=None, FlowAdvertise=None, FlowSetId=None, Name=None, NumberOfFlows=None):
        """Finds and retrieves flowSet resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve flowSet resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all flowSet resources from the server.

        Args
        ----
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offers more context
        - FlowAdvertise (bool): If selected, the flows are advertised by the OF Channel.
        - FlowSetId (str): Specify the controller Flow Set identifier.
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NumberOfFlows (number): The number of flows to be configured for the controller table.

        Returns
        -------
        - self: This instance with matching flowSet resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of flowSet data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the flowSet resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def get_device_ids(self, PortNames=None, Active=None, Cookie=None, CookieMask=None, FlowFlags=None, FlowMatchType=None, HardTimeout=None, IdleTimeout=None, Priority=None):
        """Base class infrastructure that gets a list of flowSet device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active
        - Cookie (str): optional regex of cookie
        - CookieMask (str): optional regex of cookieMask
        - FlowFlags (str): optional regex of flowFlags
        - FlowMatchType (str): optional regex of flowMatchType
        - HardTimeout (str): optional regex of hardTimeout
        - IdleTimeout (str): optional regex of idleTimeout
        - Priority (str): optional regex of priority

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
