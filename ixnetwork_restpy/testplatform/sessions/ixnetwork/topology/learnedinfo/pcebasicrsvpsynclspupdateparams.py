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


class PceBasicRsvpSyncLspUpdateParams(Base):
    """PCE Learned LSPs Information Database
    The PceBasicRsvpSyncLspUpdateParams class encapsulates a list of pceBasicRsvpSyncLspUpdateParams resources that are managed by the system.
    A list of resources can be retrieved from the server using the PceBasicRsvpSyncLspUpdateParams.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'pceBasicRsvpSyncLspUpdateParams'

    def __init__(self, parent):
        super(PceBasicRsvpSyncLspUpdateParams, self).__init__(parent)

    @property
    def PceUpdateRsvpEroSubObjectList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.pceupdatersvperosubobjectlist.PceUpdateRsvpEroSubObjectList): An instance of the PceUpdateRsvpEroSubObjectList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.pceupdatersvperosubobjectlist import PceUpdateRsvpEroSubObjectList
        return PceUpdateRsvpEroSubObjectList(self)

    @property
    def PceUpdateRsvpMetricSubObjectList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.pceupdatersvpmetricsubobjectlist.PceUpdateRsvpMetricSubObjectList): An instance of the PceUpdateRsvpMetricSubObjectList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.pceupdatersvpmetricsubobjectlist import PceUpdateRsvpMetricSubObjectList
        return PceUpdateRsvpMetricSubObjectList(self)

    @property
    def PceUpdateXroSubObjectList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.pceupdatexrosubobjectlist.PceUpdateXroSubObjectList): An instance of the PceUpdateXroSubObjectList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.pceupdatexrosubobjectlist import PceUpdateXroSubObjectList
        return PceUpdateXroSubObjectList(self)

    @property
    def Bandwidth(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Bandwidth (bps)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('bandwidth'))

    @property
    def BindingType(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Indicates the type of binding included in the TLV. Types are as follows: 20bit MPLS Label 32bit MPLS Label. Default value is 20bit MPLS Label.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('bindingType'))

    @property
    def Bos(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This bit is set to True for the last entry in the label stack i.e., for the bottom of the stack, and False for all other label stack entries. This control will be editable only if Binding Type is MPLS Label 32bit.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('bos'))

    @property
    def ConfigureBandwidth(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Configure Bandwidth
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('configureBandwidth'))

    @property
    def ConfigureEro(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Configure ERO
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('configureEro'))

    @property
    def ConfigureLsp(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Configure LSP
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('configureLsp'))

    @property
    def ConfigureLspa(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Configure LSPA
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('configureLspa'))

    @property
    def ConfigureMetric(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Configure Metric
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('configureMetric'))

    @property
    def ExcludeAny(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Exclude Any
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('excludeAny'))

    @property
    def HoldingPriority(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Holding Priority
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('holdingPriority'))

    @property
    def IncludeAll(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Include All
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('includeAll'))

    @property
    def IncludeAny(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Include Any
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('includeAny'))

    @property
    def IncludeSrp(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Indicates whether SRP object will be included in a PCInitiate message. All other attributes in sub-tab-SRP would be editable only if this checkbox is enabled.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('includeSrp'))

    @property
    def IncludeSymbolicPathName(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Indicates if Symbolic-Path-Name TLV is to be included in PCUpate trigger message.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('includeSymbolicPathName'))

    @property
    def IncludeTEPathBindingTLV(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Indicates if TE-PATH-BINDING TLV is to be included in PCUpate trigger message.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('includeTEPathBindingTLV'))

    @property
    def IncludeXro(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Indicates whether XRO object will be included in a PcUpdate message. All other attributes in sub-tab Update XRO would be editable only if this checkbox is enabled.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('includeXro'))

    @property
    def LocalProtection(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Local Protection
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('localProtection'))

    @property
    def MplsLabel(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This control will be editable if the Binding Type is set to either 20bit or 32bit MPLS-Label. This field will take the 20bit value of the MPLS-Label
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('mplsLabel'))

    @property
    def NumberOfEroSubObjects(self):
        """
        Returns
        -------
        - number: Value that indicates the number of ERO Sub Objects to be configured.
        """
        return self._get_attribute('numberOfEroSubObjects')
    @NumberOfEroSubObjects.setter
    def NumberOfEroSubObjects(self, value):
        self._set_attribute('numberOfEroSubObjects', value)

    @property
    def NumberOfMetricSubObjects(self):
        """
        Returns
        -------
        - number: Value that indicates the number of Metric Objects to be configured.
        """
        return self._get_attribute('numberOfMetricSubObjects')
    @NumberOfMetricSubObjects.setter
    def NumberOfMetricSubObjects(self, value):
        self._set_attribute('numberOfMetricSubObjects', value)

    @property
    def NumberOfXroSubObjects(self):
        """
        Returns
        -------
        - number: Value that indicates the number of XRO Sub Objects to be configured.
        """
        return self._get_attribute('numberOfXroSubObjects')
    @NumberOfXroSubObjects.setter
    def NumberOfXroSubObjects(self, value):
        self._set_attribute('numberOfXroSubObjects', value)

    @property
    def OverridePLSPID(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Allows the user to Send PcUpdate with an unknown PLSP-ID
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('overridePLSPID'))

    @property
    def OverrideSrpId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Indicates whether SRP object will be included in a PCUpdate trigger parameters. All other attributes in sub-tab-SRP would be editable only if this checkbox is enabled.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('overrideSrpId'))

    @property
    def PceTriggersChoiceList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Based on options selected, IxNetwork sends information to PCPU and refreshes the statistical data in the corresponding tab of Learned Information
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('pceTriggersChoiceList'))

    @property
    def PlspIdTriggerParam(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The value of PLSP-ID that should be put in the PcUpdate Message
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('plspIdTriggerParam'))

    @property
    def SendEmptyTLV(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If enabled all fields after Binding Type will be grayed out.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('sendEmptyTLV'))

    @property
    def SetupPriority(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Setup Priority
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('setupPriority'))

    @property
    def SrpId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The SRP object is used to correlate between initiation requests sent by the PCE and the error reports and state reports sent by the PCC. This number is unique per PCEP session and is incremented per initiation.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('srpId'))

    @property
    def Tc(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This field is used to carry traffic class information. This control will be editable only if Binding Type is MPLS Label 32bit.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('tc'))

    @property
    def Ttl(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This field is used to encode a time-to-live value. This control will be editable only if Binding Type is MPLS Label 32bit.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('ttl'))

    @property
    def XroFailBit(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): XRO Fail bit
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('xroFailBit'))

    def update(self, NumberOfEroSubObjects=None, NumberOfMetricSubObjects=None, NumberOfXroSubObjects=None):
        """Updates pceBasicRsvpSyncLspUpdateParams resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - NumberOfEroSubObjects (number): Value that indicates the number of ERO Sub Objects to be configured.
        - NumberOfMetricSubObjects (number): Value that indicates the number of Metric Objects to be configured.
        - NumberOfXroSubObjects (number): Value that indicates the number of XRO Sub Objects to be configured.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(locals())

    def find(self, NumberOfEroSubObjects=None, NumberOfMetricSubObjects=None, NumberOfXroSubObjects=None):
        """Finds and retrieves pceBasicRsvpSyncLspUpdateParams resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve pceBasicRsvpSyncLspUpdateParams resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all pceBasicRsvpSyncLspUpdateParams resources from the server.

        Args
        ----
        - NumberOfEroSubObjects (number): Value that indicates the number of ERO Sub Objects to be configured.
        - NumberOfMetricSubObjects (number): Value that indicates the number of Metric Objects to be configured.
        - NumberOfXroSubObjects (number): Value that indicates the number of XRO Sub Objects to be configured.

        Returns
        -------
        - self: This instance with matching pceBasicRsvpSyncLspUpdateParams resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of pceBasicRsvpSyncLspUpdateParams data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the pceBasicRsvpSyncLspUpdateParams resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def get_device_ids(self, PortNames=None, Bandwidth=None, BindingType=None, Bos=None, ConfigureBandwidth=None, ConfigureEro=None, ConfigureLsp=None, ConfigureLspa=None, ConfigureMetric=None, ExcludeAny=None, HoldingPriority=None, IncludeAll=None, IncludeAny=None, IncludeSrp=None, IncludeSymbolicPathName=None, IncludeTEPathBindingTLV=None, IncludeXro=None, LocalProtection=None, MplsLabel=None, OverridePLSPID=None, OverrideSrpId=None, PceTriggersChoiceList=None, PlspIdTriggerParam=None, SendEmptyTLV=None, SetupPriority=None, SrpId=None, Tc=None, Ttl=None, XroFailBit=None):
        """Base class infrastructure that gets a list of pceBasicRsvpSyncLspUpdateParams device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Bandwidth (str): optional regex of bandwidth
        - BindingType (str): optional regex of bindingType
        - Bos (str): optional regex of bos
        - ConfigureBandwidth (str): optional regex of configureBandwidth
        - ConfigureEro (str): optional regex of configureEro
        - ConfigureLsp (str): optional regex of configureLsp
        - ConfigureLspa (str): optional regex of configureLspa
        - ConfigureMetric (str): optional regex of configureMetric
        - ExcludeAny (str): optional regex of excludeAny
        - HoldingPriority (str): optional regex of holdingPriority
        - IncludeAll (str): optional regex of includeAll
        - IncludeAny (str): optional regex of includeAny
        - IncludeSrp (str): optional regex of includeSrp
        - IncludeSymbolicPathName (str): optional regex of includeSymbolicPathName
        - IncludeTEPathBindingTLV (str): optional regex of includeTEPathBindingTLV
        - IncludeXro (str): optional regex of includeXro
        - LocalProtection (str): optional regex of localProtection
        - MplsLabel (str): optional regex of mplsLabel
        - OverridePLSPID (str): optional regex of overridePLSPID
        - OverrideSrpId (str): optional regex of overrideSrpId
        - PceTriggersChoiceList (str): optional regex of pceTriggersChoiceList
        - PlspIdTriggerParam (str): optional regex of plspIdTriggerParam
        - SendEmptyTLV (str): optional regex of sendEmptyTLV
        - SetupPriority (str): optional regex of setupPriority
        - SrpId (str): optional regex of srpId
        - Tc (str): optional regex of tc
        - Ttl (str): optional regex of ttl
        - XroFailBit (str): optional regex of xroFailBit

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())

    def SendPcUpdate(self, *args, **kwargs):
        """Executes the sendPcUpdate operation on the server.

        Counts property changes created by the user.

        sendPcUpdate(Arg2=list)list
        ---------------------------
        - Arg2 (list(number)): List of indices into the learned information corresponding to trigger data.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('sendPcUpdate', payload=payload, response_object=None)

    def SendReturnDelegation(self, *args, **kwargs):
        """Executes the sendReturnDelegation operation on the server.

        Counts property changes created by the user.

        sendReturnDelegation(Arg2=list)list
        -----------------------------------
        - Arg2 (list(number)): List of indices into the learned information corresponding to trigger data.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('sendReturnDelegation', payload=payload, response_object=None)
