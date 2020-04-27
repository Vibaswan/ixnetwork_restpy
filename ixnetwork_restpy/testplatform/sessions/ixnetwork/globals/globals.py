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


class Globals(Base):
    """This object holds the configurable global values of IxNetwork for interfaces and the protocol stack.
    The Globals class encapsulates a required globals resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'globals'

    def __init__(self, parent):
        super(Globals, self).__init__(parent)

    @property
    def AppErrors(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.apperrors.apperrors.AppErrors): An instance of the AppErrors class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.apperrors.apperrors import AppErrors
        return AppErrors(self)

    @property
    def Diagnostics(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.diagnostics.diagnostics.Diagnostics): An instance of the Diagnostics class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.diagnostics.diagnostics import Diagnostics
        return Diagnostics(self)._select()

    @property
    def Interfaces(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.interfaces.interfaces.Interfaces): An instance of the Interfaces class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.interfaces.interfaces import Interfaces
        return Interfaces(self)._select()

    @property
    def Ixnet(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.ixnet.ixnet.Ixnet): An instance of the Ixnet class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.ixnet.ixnet import Ixnet
        return Ixnet(self)._select()

    @property
    def Licensing(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.licensing.licensing.Licensing): An instance of the Licensing class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.licensing.licensing import Licensing
        return Licensing(self)._select()

    @property
    def Preferences(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.preferences.preferences.Preferences): An instance of the Preferences class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.preferences.preferences import Preferences
        return Preferences(self)._select()

    @property
    def ProtocolStack(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.protocolstack.ProtocolStack): An instance of the ProtocolStack class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.protocolstack import ProtocolStack
        return ProtocolStack(self)._select()

    @property
    def Scriptgen(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.scriptgen.scriptgen.Scriptgen): An instance of the Scriptgen class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.scriptgen.scriptgen import Scriptgen
        return Scriptgen(self)._select()

    @property
    def TestInspector(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.testinspector.testinspector.TestInspector): An instance of the TestInspector class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.testinspector.testinspector import TestInspector
        return TestInspector(self)._select()

    @property
    def Topology(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.topology.Topology): An instance of the Topology class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.topology import Topology
        return Topology(self)._select()

    @property
    def BuildNumber(self):
        """
        Returns
        -------
        - str: The IxNetwork software build number.
        """
        return self._get_attribute('buildNumber')

    @property
    def CommandArgs(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute('commandArgs')

    @property
    def ConfigFileName(self):
        """
        Returns
        -------
        - str: The name of the configuration file.
        """
        return self._get_attribute('configFileName')

    @property
    def ConfigSummary(self):
        """
        Returns
        -------
        - list(dict(arg1:str,arg2:str,arg3:list[dict(arg1:str,arg2:str)])): A high level summary description of the currently loaded configuration
        """
        return self._get_attribute('configSummary')

    @property
    def IsConfigDifferent(self):
        """
        Returns
        -------
        - bool: (Read only) If true, then the current IxNetwork configuration is different than the configuration that was previously loaded.
        """
        return self._get_attribute('isConfigDifferent')

    @property
    def IxosBuildNumber(self):
        """
        Returns
        -------
        - str: The IxOS software build number.
        """
        return self._get_attribute('ixosBuildNumber')

    @property
    def PersistencePath(self):
        """
        Returns
        -------
        - str: This attribute returns a directory of the IxNetwork API server machine, where users can drop their files from the client scripts using IxNetwork APIs. To Put files in this directory, users do not require to run IxNetwork API server in administrative mode
        """
        return self._get_attribute('persistencePath')

    @property
    def ProtocolbuildNumber(self):
        """
        Returns
        -------
        - str: The build number of the protocol.
        """
        return self._get_attribute('protocolbuildNumber')

    @property
    def Username(self):
        """
        Returns
        -------
        - str: The name of the user.
        """
        return self._get_attribute('username')
