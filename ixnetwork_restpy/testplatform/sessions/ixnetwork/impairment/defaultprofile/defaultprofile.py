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


class DefaultProfile(Base):
    """The default behavior for packets which are not handled by any other profile.
    The DefaultProfile class encapsulates a required defaultProfile resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'defaultProfile'
    _SDM_ATT_MAP = {
        'Name': 'name',
    }

    def __init__(self, parent):
        super(DefaultProfile, self).__init__(parent)

    @property
    def BitError(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.impairment.defaultprofile.biterror.biterror.BitError): An instance of the BitError class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.impairment.defaultprofile.biterror.biterror import BitError
        if self._properties.get('BitError', None) is None:
            return BitError(self)._select()
        else:
            return self._properties.get('BitError')

    @property
    def Checksums(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.impairment.defaultprofile.checksums.checksums.Checksums): An instance of the Checksums class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.impairment.defaultprofile.checksums.checksums import Checksums
        if self._properties.get('Checksums', None) is None:
            return Checksums(self)._select()
        else:
            return self._properties.get('Checksums')

    @property
    def CustomDelayVariation(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.impairment.defaultprofile.customdelayvariation.customdelayvariation.CustomDelayVariation): An instance of the CustomDelayVariation class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.impairment.defaultprofile.customdelayvariation.customdelayvariation import CustomDelayVariation
        if self._properties.get('CustomDelayVariation', None) is None:
            return CustomDelayVariation(self)._select()
        else:
            return self._properties.get('CustomDelayVariation')

    @property
    def Delay(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.impairment.defaultprofile.delay.delay.Delay): An instance of the Delay class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.impairment.defaultprofile.delay.delay import Delay
        if self._properties.get('Delay', None) is None:
            return Delay(self)._select()
        else:
            return self._properties.get('Delay')

    @property
    def DelayVariation(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.impairment.defaultprofile.delayvariation.delayvariation.DelayVariation): An instance of the DelayVariation class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.impairment.defaultprofile.delayvariation.delayvariation import DelayVariation
        if self._properties.get('DelayVariation', None) is None:
            return DelayVariation(self)._select()
        else:
            return self._properties.get('DelayVariation')

    @property
    def Drop(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.impairment.defaultprofile.drop.drop.Drop): An instance of the Drop class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.impairment.defaultprofile.drop.drop import Drop
        if self._properties.get('Drop', None) is None:
            return Drop(self)._select()
        else:
            return self._properties.get('Drop')

    @property
    def Duplicate(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.impairment.defaultprofile.duplicate.duplicate.Duplicate): An instance of the Duplicate class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.impairment.defaultprofile.duplicate.duplicate import Duplicate
        if self._properties.get('Duplicate', None) is None:
            return Duplicate(self)._select()
        else:
            return self._properties.get('Duplicate')

    @property
    def Modifier(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.impairment.defaultprofile.modifier.modifier.Modifier): An instance of the Modifier class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.impairment.defaultprofile.modifier.modifier import Modifier
        if self._properties.get('Modifier', None) is None:
            return Modifier(self)
        else:
            return self._properties.get('Modifier')

    @property
    def Reorder(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.impairment.defaultprofile.reorder.reorder.Reorder): An instance of the Reorder class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.impairment.defaultprofile.reorder.reorder import Reorder
        if self._properties.get('Reorder', None) is None:
            return Reorder(self)._select()
        else:
            return self._properties.get('Reorder')

    @property
    def RxRateLimit(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.impairment.defaultprofile.rxratelimit.rxratelimit.RxRateLimit): An instance of the RxRateLimit class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.impairment.defaultprofile.rxratelimit.rxratelimit import RxRateLimit
        if self._properties.get('RxRateLimit', None) is None:
            return RxRateLimit(self)._select()
        else:
            return self._properties.get('RxRateLimit')

    @property
    def Name(self):
        """
        Returns
        -------
        - str: The name of the profile. Read-only.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Name'])
