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


class HostTopologyLearnedInformation(Base):
    """NOT DEFINED
    The HostTopologyLearnedInformation class encapsulates a required hostTopologyLearnedInformation resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'hostTopologyLearnedInformation'
    _SDM_ATT_MAP = {
    }

    def __init__(self, parent):
        super(HostTopologyLearnedInformation, self).__init__(parent)

    @property
    def SwitchHostRangeLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchhostrangelearnedinfo_4b8cdab80884ed8a3ce6bf35f9235d28.SwitchHostRangeLearnedInfo): An instance of the SwitchHostRangeLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchhostrangelearnedinfo_4b8cdab80884ed8a3ce6bf35f9235d28 import SwitchHostRangeLearnedInfo
        if self._properties.get('SwitchHostRangeLearnedInfo', None) is None:
            return SwitchHostRangeLearnedInfo(self)
        else:
            return self._properties.get('SwitchHostRangeLearnedInfo')

    @property
    def SwitchHostRangeLearnedInfoTriggerAttributes(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchhostrangelearnedinfotriggerattributes_972a89638b94fd8481cd311e99101fb6.SwitchHostRangeLearnedInfoTriggerAttributes): An instance of the SwitchHostRangeLearnedInfoTriggerAttributes class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchhostrangelearnedinfotriggerattributes_972a89638b94fd8481cd311e99101fb6 import SwitchHostRangeLearnedInfoTriggerAttributes
        if self._properties.get('SwitchHostRangeLearnedInfoTriggerAttributes', None) is None:
            return SwitchHostRangeLearnedInfoTriggerAttributes(self)._select()
        else:
            return self._properties.get('SwitchHostRangeLearnedInfoTriggerAttributes')

    def RefreshHostRangeLearnedInformation(self):
        """Executes the refreshHostRangeLearnedInformation operation on the server.

        NOT DEFINED

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('refreshHostRangeLearnedInformation', payload=payload, response_object=None)
