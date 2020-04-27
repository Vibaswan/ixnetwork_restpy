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


class NetTopologyLinear(Base):
    """Linear topology
    The NetTopologyLinear class encapsulates a list of netTopologyLinear resources that are managed by the user.
    A list of resources can be retrieved from the server using the NetTopologyLinear.find() method.
    The list can be managed by using the NetTopologyLinear.add() and NetTopologyLinear.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'netTopologyLinear'

    def __init__(self, parent):
        super(NetTopologyLinear, self).__init__(parent)

    @property
    def IncludeEntryPoint(self):
        """
        Returns
        -------
        - bool: if true, entry node belongs to ring topology, otherwise it is outside of ring
        """
        return self._get_attribute('includeEntryPoint')
    @IncludeEntryPoint.setter
    def IncludeEntryPoint(self, value):
        self._set_attribute('includeEntryPoint', value)

    @property
    def LinkMultiplier(self):
        """
        Returns
        -------
        - number: number of links between two nodes
        """
        return self._get_attribute('linkMultiplier')
    @LinkMultiplier.setter
    def LinkMultiplier(self, value):
        self._set_attribute('linkMultiplier', value)

    @property
    def Nodes(self):
        """
        Returns
        -------
        - number: number of nodes
        """
        return self._get_attribute('nodes')
    @Nodes.setter
    def Nodes(self, value):
        self._set_attribute('nodes', value)

    def update(self, IncludeEntryPoint=None, LinkMultiplier=None, Nodes=None):
        """Updates netTopologyLinear resource on the server.

        Args
        ----
        - IncludeEntryPoint (bool): if true, entry node belongs to ring topology, otherwise it is outside of ring
        - LinkMultiplier (number): number of links between two nodes
        - Nodes (number): number of nodes

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(locals())

    def add(self, IncludeEntryPoint=None, LinkMultiplier=None, Nodes=None):
        """Adds a new netTopologyLinear resource on the server and adds it to the container.

        Args
        ----
        - IncludeEntryPoint (bool): if true, entry node belongs to ring topology, otherwise it is outside of ring
        - LinkMultiplier (number): number of links between two nodes
        - Nodes (number): number of nodes

        Returns
        -------
        - self: This instance with all currently retrieved netTopologyLinear resources using find and the newly added netTopologyLinear resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(locals())

    def remove(self):
        """Deletes all the contained netTopologyLinear resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, IncludeEntryPoint=None, LinkMultiplier=None, Nodes=None):
        """Finds and retrieves netTopologyLinear resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve netTopologyLinear resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all netTopologyLinear resources from the server.

        Args
        ----
        - IncludeEntryPoint (bool): if true, entry node belongs to ring topology, otherwise it is outside of ring
        - LinkMultiplier (number): number of links between two nodes
        - Nodes (number): number of nodes

        Returns
        -------
        - self: This instance with matching netTopologyLinear resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of netTopologyLinear data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the netTopologyLinear resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
