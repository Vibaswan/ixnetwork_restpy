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


class Mld(Base):
    """This object sends and responds to MLD messages.
    The Mld class encapsulates a required mld resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'mld'

    def __init__(self, parent):
        super(Mld, self).__init__(parent)

    @property
    def Host(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.host_8648a0e7de3912b38570b645c1136c7d.Host): An instance of the Host class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.host_8648a0e7de3912b38570b645c1136c7d import Host
        return Host(self)

    @property
    def Querier(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.querier_74ff7136f0418ace9808c23a02b43ab2.Querier): An instance of the Querier class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.querier_74ff7136f0418ace9808c23a02b43ab2 import Querier
        return Querier(self)

    @property
    def EnableDoneOnStop(self):
        """
        Returns
        -------
        - bool: Controls the behavior of MLD messages.
        """
        return self._get_attribute('enableDoneOnStop')
    @EnableDoneOnStop.setter
    def EnableDoneOnStop(self, value):
        self._set_attribute('enableDoneOnStop', value)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: Enables or disables simulation of the router.
        """
        return self._get_attribute('enabled')
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute('enabled', value)

    @property
    def Mldv2Report(self):
        """
        Returns
        -------
        - str(type143 | type206): The version of the MLD report to be generated.
        """
        return self._get_attribute('mldv2Report')
    @Mldv2Report.setter
    def Mldv2Report(self, value):
        self._set_attribute('mldv2Report', value)

    @property
    def NumberOfGroups(self):
        """
        Returns
        -------
        - number: Provides a means of throttling the amount of MLD traffic generated by the port.
        """
        return self._get_attribute('numberOfGroups')
    @NumberOfGroups.setter
    def NumberOfGroups(self, value):
        self._set_attribute('numberOfGroups', value)

    @property
    def NumberOfQueries(self):
        """
        Returns
        -------
        - number: Provides a means of throttling the amount of MLD queries generated by the port.
        """
        return self._get_attribute('numberOfQueries')
    @NumberOfQueries.setter
    def NumberOfQueries(self, value):
        self._set_attribute('numberOfQueries', value)

    @property
    def QueryTimePeriod(self):
        """
        Returns
        -------
        - number: The time, in milliseconds, between queries.
        """
        return self._get_attribute('queryTimePeriod')
    @QueryTimePeriod.setter
    def QueryTimePeriod(self, value):
        self._set_attribute('queryTimePeriod', value)

    @property
    def RunningState(self):
        """
        Returns
        -------
        - str(unknown | stopped | stopping | starting | started): The current running state of the MLD server.
        """
        return self._get_attribute('runningState')

    @property
    def TimePeriod(self):
        """
        Returns
        -------
        - number: Specify the length of each time period during which the specified number of MLD Groups will be advertised.
        """
        return self._get_attribute('timePeriod')
    @TimePeriod.setter
    def TimePeriod(self, value):
        self._set_attribute('timePeriod', value)

    def update(self, EnableDoneOnStop=None, Enabled=None, Mldv2Report=None, NumberOfGroups=None, NumberOfQueries=None, QueryTimePeriod=None, TimePeriod=None):
        """Updates mld resource on the server.

        Args
        ----
        - EnableDoneOnStop (bool): Controls the behavior of MLD messages.
        - Enabled (bool): Enables or disables simulation of the router.
        - Mldv2Report (str(type143 | type206)): The version of the MLD report to be generated.
        - NumberOfGroups (number): Provides a means of throttling the amount of MLD traffic generated by the port.
        - NumberOfQueries (number): Provides a means of throttling the amount of MLD queries generated by the port.
        - QueryTimePeriod (number): The time, in milliseconds, between queries.
        - TimePeriod (number): Specify the length of each time period during which the specified number of MLD Groups will be advertised.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(locals())

    def Start(self):
        """Executes the start operation on the server.

        Starts the MLD protocol on a port or group of ports simultaneously.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('start', payload=payload, response_object=None)

    def Stop(self):
        """Executes the stop operation on the server.

        Stops the MLD protocol on a port or group of ports simultaneously.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('stop', payload=payload, response_object=None)
