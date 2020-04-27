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


class Chassis(Base):
    """The chassis command is used to add a new chassis to a chain of chassis, configure an existing chassis or delete an existing one from the chain in use.
    The Chassis class encapsulates a list of chassis resources that are managed by the user.
    A list of resources can be retrieved from the server using the Chassis.find() method.
    The list can be managed by using the Chassis.add() and Chassis.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'chassis'

    def __init__(self, parent):
        super(Chassis, self).__init__(parent)

    @property
    def Card(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.availablehardware.chassis.card.card.Card): An instance of the Card class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.availablehardware.chassis.card.card import Card
        return Card(self)

    @property
    def CableLength(self):
        """
        Returns
        -------
        - number: Specifies the length of the cable between two adjacent chassis. Must be set only after the chassis hostname has been set and committed on the current chassis.
        """
        return self._get_attribute('cableLength')
    @CableLength.setter
    def CableLength(self, value):
        self._set_attribute('cableLength', value)

    @property
    def ChainTopology(self):
        """
        Returns
        -------
        - str(daisy | none | star): The chain topology type. This must be defined on the master chassis. It must be defined only after the chassis host name has been specified and applied on the current chassis. For legacy chassis chains, the daisy chainTopology should be indicated.
        """
        return self._get_attribute('chainTopology')
    @ChainTopology.setter
    def ChainTopology(self, value):
        self._set_attribute('chainTopology', value)

    @property
    def ChassisOSType(self):
        """
        Returns
        -------
        - str(linux | unknown | windows): 
        """
        return self._get_attribute('chassisOSType')

    @property
    def ChassisType(self):
        """
        Returns
        -------
        - str: The type of chassis.
        """
        return self._get_attribute('chassisType')

    @property
    def ChassisVersion(self):
        """
        Returns
        -------
        - str: The version of the Chassis in use.
        """
        return self._get_attribute('chassisVersion')

    @property
    def ConnectRetries(self):
        """
        Returns
        -------
        - number: The number of time the client attempted to re-connect with the chassis. (read only)
        """
        return self._get_attribute('connectRetries')

    @property
    def Hostname(self):
        """
        Returns
        -------
        - str: The IP address associated with the chassis.
        """
        return self._get_attribute('hostname')
    @Hostname.setter
    def Hostname(self, value):
        self._set_attribute('hostname', value)

    @property
    def Ip(self):
        """
        Returns
        -------
        - str: The IP address associated with the chassis.
        """
        return self._get_attribute('ip')

    @property
    def IsLicensesRetrieved(self):
        """
        Returns
        -------
        - bool: Retrieves the licenses in the chassis.
        """
        return self._get_attribute('isLicensesRetrieved')

    @property
    def IsMaster(self):
        """
        Returns
        -------
        - bool: Specifies whether this chassis is a master of a slave in a chain. There can be only one master chassis in a chain. NOTE: The master is automatically assigned based on cable connections.
        """
        return self._get_attribute('isMaster')

    @property
    def IxnBuildNumber(self):
        """
        Returns
        -------
        - str: IxNetwork build number.
        """
        return self._get_attribute('ixnBuildNumber')

    @property
    def IxosBuildNumber(self):
        """
        Returns
        -------
        - str: The IxOS version of the Chassis in use.
        """
        return self._get_attribute('ixosBuildNumber')

    @property
    def LicenseErrors(self):
        """
        Returns
        -------
        - list(str): Shows the licening errors that occurred due to licensing problems.
        """
        return self._get_attribute('licenseErrors')

    @property
    def MasterChassis(self):
        """
        Returns
        -------
        - str: Specify the hostname of the master chassis on a slave chassis. Must be left blank on master. Must be set only after the chassis hostname has been set and committed on the current chassis.
        """
        return self._get_attribute('masterChassis')
    @MasterChassis.setter
    def MasterChassis(self, value):
        self._set_attribute('masterChassis', value)

    @property
    def ProtocolBuildNumber(self):
        """
        Returns
        -------
        - str: The Protocols version of the Chassis in use.
        """
        return self._get_attribute('protocolBuildNumber')

    @property
    def SequenceId(self):
        """
        Returns
        -------
        - number: Indicates the order at which the chassis in a chassis chain are pulsed by IxOS. Star topology chains are automatically setting this value. Must be set only after the chassis hostname has been set and committed on the current chassis.
        """
        return self._get_attribute('sequenceId')
    @SequenceId.setter
    def SequenceId(self, value):
        self._set_attribute('sequenceId', value)

    @property
    def State(self):
        """
        Returns
        -------
        - str(down | down | polling | polling | polling | ready): The following states can be read from the port: polling, ready, and down.
        """
        return self._get_attribute('state')

    def update(self, CableLength=None, ChainTopology=None, Hostname=None, MasterChassis=None, SequenceId=None):
        """Updates chassis resource on the server.

        Args
        ----
        - CableLength (number): Specifies the length of the cable between two adjacent chassis. Must be set only after the chassis hostname has been set and committed on the current chassis.
        - ChainTopology (str(daisy | none | star)): The chain topology type. This must be defined on the master chassis. It must be defined only after the chassis host name has been specified and applied on the current chassis. For legacy chassis chains, the daisy chainTopology should be indicated.
        - Hostname (str): The IP address associated with the chassis.
        - MasterChassis (str): Specify the hostname of the master chassis on a slave chassis. Must be left blank on master. Must be set only after the chassis hostname has been set and committed on the current chassis.
        - SequenceId (number): Indicates the order at which the chassis in a chassis chain are pulsed by IxOS. Star topology chains are automatically setting this value. Must be set only after the chassis hostname has been set and committed on the current chassis.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(locals())

    def add(self, CableLength=None, ChainTopology=None, Hostname=None, MasterChassis=None, SequenceId=None):
        """Adds a new chassis resource on the server and adds it to the container.

        Args
        ----
        - CableLength (number): Specifies the length of the cable between two adjacent chassis. Must be set only after the chassis hostname has been set and committed on the current chassis.
        - ChainTopology (str(daisy | none | star)): The chain topology type. This must be defined on the master chassis. It must be defined only after the chassis host name has been specified and applied on the current chassis. For legacy chassis chains, the daisy chainTopology should be indicated.
        - Hostname (str): The IP address associated with the chassis.
        - MasterChassis (str): Specify the hostname of the master chassis on a slave chassis. Must be left blank on master. Must be set only after the chassis hostname has been set and committed on the current chassis.
        - SequenceId (number): Indicates the order at which the chassis in a chassis chain are pulsed by IxOS. Star topology chains are automatically setting this value. Must be set only after the chassis hostname has been set and committed on the current chassis.

        Returns
        -------
        - self: This instance with all currently retrieved chassis resources using find and the newly added chassis resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(locals())

    def remove(self):
        """Deletes all the contained chassis resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, CableLength=None, ChainTopology=None, ChassisOSType=None, ChassisType=None, ChassisVersion=None, ConnectRetries=None, Hostname=None, Ip=None, IsLicensesRetrieved=None, IsMaster=None, IxnBuildNumber=None, IxosBuildNumber=None, LicenseErrors=None, MasterChassis=None, ProtocolBuildNumber=None, SequenceId=None, State=None):
        """Finds and retrieves chassis resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve chassis resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all chassis resources from the server.

        Args
        ----
        - CableLength (number): Specifies the length of the cable between two adjacent chassis. Must be set only after the chassis hostname has been set and committed on the current chassis.
        - ChainTopology (str(daisy | none | star)): The chain topology type. This must be defined on the master chassis. It must be defined only after the chassis host name has been specified and applied on the current chassis. For legacy chassis chains, the daisy chainTopology should be indicated.
        - ChassisOSType (str(linux | unknown | windows)): 
        - ChassisType (str): The type of chassis.
        - ChassisVersion (str): The version of the Chassis in use.
        - ConnectRetries (number): The number of time the client attempted to re-connect with the chassis. (read only)
        - Hostname (str): The IP address associated with the chassis.
        - Ip (str): The IP address associated with the chassis.
        - IsLicensesRetrieved (bool): Retrieves the licenses in the chassis.
        - IsMaster (bool): Specifies whether this chassis is a master of a slave in a chain. There can be only one master chassis in a chain. NOTE: The master is automatically assigned based on cable connections.
        - IxnBuildNumber (str): IxNetwork build number.
        - IxosBuildNumber (str): The IxOS version of the Chassis in use.
        - LicenseErrors (list(str)): Shows the licening errors that occurred due to licensing problems.
        - MasterChassis (str): Specify the hostname of the master chassis on a slave chassis. Must be left blank on master. Must be set only after the chassis hostname has been set and committed on the current chassis.
        - ProtocolBuildNumber (str): The Protocols version of the Chassis in use.
        - SequenceId (number): Indicates the order at which the chassis in a chassis chain are pulsed by IxOS. Star topology chains are automatically setting this value. Must be set only after the chassis hostname has been set and committed on the current chassis.
        - State (str(down | down | polling | polling | polling | ready)): The following states can be read from the port: polling, ready, and down.

        Returns
        -------
        - self: This instance with matching chassis resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of chassis data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the chassis resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def GetTapSettings(self):
        """Executes the getTapSettings operation on the server.

        Get TAP Settings for the given chassis

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        return self._execute('getTapSettings', payload=payload, response_object=None)

    def RefreshInfo(self):
        """Executes the refreshInfo operation on the server.

        Refresh the hardware information.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        return self._execute('refreshInfo', payload=payload, response_object=None)

    def SetTapSettings(self):
        """Executes the setTapSettings operation on the server.

        Send TAP Settings to IxServer for the given chassis.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        return self._execute('setTapSettings', payload=payload, response_object=None)
