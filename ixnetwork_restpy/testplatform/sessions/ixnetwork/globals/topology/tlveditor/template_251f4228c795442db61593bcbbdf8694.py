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


class Template(Base):
    """Tlv template container
    The Template class encapsulates a list of template resources that are managed by the user.
    A list of resources can be retrieved from the server using the Template.find() method.
    The list can be managed by using the Template.add() and Template.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'template'
    _SDM_ATT_MAP = {
        'Name': 'name',
    }

    def __init__(self, parent):
        super(Template, self).__init__(parent)

    @property
    def Tlv(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.tlveditor.tlv_485a5849242c96601ea954c1e6fdcfe5.Tlv): An instance of the Tlv class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.tlveditor.tlv_485a5849242c96601ea954c1e6fdcfe5 import Tlv
        if self._properties.get('Tlv', None) is None:
            return Tlv(self)
        else:
            return self._properties.get('Tlv')

    @property
    def Name(self):
        """
        Returns
        -------
        - str: The name of the template
        """
        return self._get_attribute(self._SDM_ATT_MAP['Name'])
    @Name.setter
    def Name(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Name'], value)

    def update(self, Name=None):
        """Updates template resource on the server.

        Args
        ----
        - Name (str): The name of the template

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Name=None):
        """Adds a new template resource on the server and adds it to the container.

        Args
        ----
        - Name (str): The name of the template

        Returns
        -------
        - self: This instance with all currently retrieved template resources using find and the newly added template resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained template resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Name=None):
        """Finds and retrieves template resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve template resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all template resources from the server.

        Args
        ----
        - Name (str): The name of the template

        Returns
        -------
        - self: This instance with matching template resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of template data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the template resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
