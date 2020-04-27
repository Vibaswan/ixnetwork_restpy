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


class DmLearnedInfo(Base):
    """This object holds lists of the dm learned information.
    The DmLearnedInfo class encapsulates a list of dmLearnedInfo resources that are managed by the system.
    A list of resources can be retrieved from the server using the DmLearnedInfo.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'dmLearnedInfo'

    def __init__(self, parent):
        super(DmLearnedInfo, self).__init__(parent)

    @property
    def AverageLooseRtt(self):
        """
        Returns
        -------
        - str: This signifies the average loose RTT.
        """
        return self._get_attribute('averageLooseRtt')

    @property
    def AverageLooseRttVariation(self):
        """
        Returns
        -------
        - str: This signifies the average loose RTT variation.
        """
        return self._get_attribute('averageLooseRttVariation')

    @property
    def AverageStrictRtt(self):
        """
        Returns
        -------
        - str: This signifies the average strict RTT.
        """
        return self._get_attribute('averageStrictRtt')

    @property
    def AverageStrictRttVariation(self):
        """
        Returns
        -------
        - str: This signifies the average strict RTT variation.
        """
        return self._get_attribute('averageStrictRttVariation')

    @property
    def DmQueriesSent(self):
        """
        Returns
        -------
        - number: This signifies the number of DM queries sent.
        """
        return self._get_attribute('dmQueriesSent')

    @property
    def DmResponsesReceived(self):
        """
        Returns
        -------
        - number: This signifies the total number of DM responses received.
        """
        return self._get_attribute('dmResponsesReceived')

    @property
    def IncomingLabelOuterInner(self):
        """
        Returns
        -------
        - str: This signifies the incoming label information.
        """
        return self._get_attribute('incomingLabelOuterInner')

    @property
    def MaxLooseRtt(self):
        """
        Returns
        -------
        - str: This signifies the maximum loose RTT.
        """
        return self._get_attribute('maxLooseRtt')

    @property
    def MaxStrictRtt(self):
        """
        Returns
        -------
        - str: This signifies the maximum strict RTT.
        """
        return self._get_attribute('maxStrictRtt')

    @property
    def MinLooseRtt(self):
        """
        Returns
        -------
        - str: This signifies the minimum loose RTT.
        """
        return self._get_attribute('minLooseRtt')

    @property
    def MinStrictRtt(self):
        """
        Returns
        -------
        - str: This signifies the minimum strict RTT.
        """
        return self._get_attribute('minStrictRtt')

    @property
    def OutgoingLabelOuterInner(self):
        """
        Returns
        -------
        - str: This signifies the Outgoing Label information.
        """
        return self._get_attribute('outgoingLabelOuterInner')

    @property
    def Type(self):
        """
        Returns
        -------
        - str: This signifies the type of the learned information.
        """
        return self._get_attribute('type')

    def find(self, AverageLooseRtt=None, AverageLooseRttVariation=None, AverageStrictRtt=None, AverageStrictRttVariation=None, DmQueriesSent=None, DmResponsesReceived=None, IncomingLabelOuterInner=None, MaxLooseRtt=None, MaxStrictRtt=None, MinLooseRtt=None, MinStrictRtt=None, OutgoingLabelOuterInner=None, Type=None):
        """Finds and retrieves dmLearnedInfo resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve dmLearnedInfo resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all dmLearnedInfo resources from the server.

        Args
        ----
        - AverageLooseRtt (str): This signifies the average loose RTT.
        - AverageLooseRttVariation (str): This signifies the average loose RTT variation.
        - AverageStrictRtt (str): This signifies the average strict RTT.
        - AverageStrictRttVariation (str): This signifies the average strict RTT variation.
        - DmQueriesSent (number): This signifies the number of DM queries sent.
        - DmResponsesReceived (number): This signifies the total number of DM responses received.
        - IncomingLabelOuterInner (str): This signifies the incoming label information.
        - MaxLooseRtt (str): This signifies the maximum loose RTT.
        - MaxStrictRtt (str): This signifies the maximum strict RTT.
        - MinLooseRtt (str): This signifies the minimum loose RTT.
        - MinStrictRtt (str): This signifies the minimum strict RTT.
        - OutgoingLabelOuterInner (str): This signifies the Outgoing Label information.
        - Type (str): This signifies the type of the learned information.

        Returns
        -------
        - self: This instance with matching dmLearnedInfo resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of dmLearnedInfo data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the dmLearnedInfo resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
