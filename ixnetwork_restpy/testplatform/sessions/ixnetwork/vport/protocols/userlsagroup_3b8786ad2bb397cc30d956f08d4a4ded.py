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


class UserLsaGroup(Base):
    """A list of LSAs to be included in this OSPFv3 router.
    The UserLsaGroup class encapsulates a list of userLsaGroup resources that are managed by the user.
    A list of resources can be retrieved from the server using the UserLsaGroup.find() method.
    The list can be managed by using the UserLsaGroup.add() and UserLsaGroup.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'userLsaGroup'

    def __init__(self, parent):
        super(UserLsaGroup, self).__init__(parent)

    @property
    def UserLsa(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.userlsa_7e2f5158a662fbbf29fc26d7a19228ce.UserLsa): An instance of the UserLsa class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.userlsa_7e2f5158a662fbbf29fc26d7a19228ce import UserLsa
        return UserLsa(self)

    @property
    def AreaId(self):
        """
        Returns
        -------
        - number: The area ID associated with all user LSAs in this group.
        """
        return self._get_attribute('areaId')
    @AreaId.setter
    def AreaId(self, value):
        self._set_attribute('areaId', value)

    @property
    def Description(self):
        """
        Returns
        -------
        - str: (Optional) A user-defined description for this particular User LSA Group. (For display only)
        """
        return self._get_attribute('description')
    @Description.setter
    def Description(self, value):
        self._set_attribute('description', value)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: This User LSA Group is enabled for advertising user-created LSAs.
        """
        return self._get_attribute('enabled')
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute('enabled', value)

    def update(self, AreaId=None, Description=None, Enabled=None):
        """Updates userLsaGroup resource on the server.

        Args
        ----
        - AreaId (number): The area ID associated with all user LSAs in this group.
        - Description (str): (Optional) A user-defined description for this particular User LSA Group. (For display only)
        - Enabled (bool): This User LSA Group is enabled for advertising user-created LSAs.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(locals())

    def add(self, AreaId=None, Description=None, Enabled=None):
        """Adds a new userLsaGroup resource on the server and adds it to the container.

        Args
        ----
        - AreaId (number): The area ID associated with all user LSAs in this group.
        - Description (str): (Optional) A user-defined description for this particular User LSA Group. (For display only)
        - Enabled (bool): This User LSA Group is enabled for advertising user-created LSAs.

        Returns
        -------
        - self: This instance with all currently retrieved userLsaGroup resources using find and the newly added userLsaGroup resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(locals())

    def remove(self):
        """Deletes all the contained userLsaGroup resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, AreaId=None, Description=None, Enabled=None):
        """Finds and retrieves userLsaGroup resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve userLsaGroup resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all userLsaGroup resources from the server.

        Args
        ----
        - AreaId (number): The area ID associated with all user LSAs in this group.
        - Description (str): (Optional) A user-defined description for this particular User LSA Group. (For display only)
        - Enabled (bool): This User LSA Group is enabled for advertising user-created LSAs.

        Returns
        -------
        - self: This instance with matching userLsaGroup resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of userLsaGroup data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the userLsaGroup resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
