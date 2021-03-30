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


class View(Base):
    """The root node for all statistics view per 5.40 SV API.
    The View class encapsulates a list of view resources that are managed by the user.
    A list of resources can be retrieved from the server using the View.find() method.
    The list can be managed by using the View.add() and View.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'view'
    _SDM_ATT_MAP = {
        'AutoRefresh': 'autoRefresh',
        'AutoUpdate': 'autoUpdate',
        'AvailableStatsSelectorColumns': 'availableStatsSelectorColumns',
        'Caption': 'caption',
        'CsvFileName': 'csvFileName',
        'EnableCsvLogging': 'enableCsvLogging',
        'Enabled': 'enabled',
        'EnabledStatsSelectorColumns': 'enabledStatsSelectorColumns',
        'OnDemandRefreshView': 'onDemandRefreshView',
        'PageTimeout': 'pageTimeout',
        'ReadOnly': 'readOnly',
        'StatsSelectorManager': 'statsSelectorManager',
        'TimeSeries': 'timeSeries',
        'TreeViewNodeName': 'treeViewNodeName',
        'Type': 'type',
        'TypeDescription': 'typeDescription',
        'ViewCategory': 'viewCategory',
        'Visible': 'visible',
    }

    def __init__(self, parent):
        super(View, self).__init__(parent)

    @property
    def AdvancedCVFilters(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.advancedcvfilters.advancedcvfilters.AdvancedCVFilters): An instance of the AdvancedCVFilters class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.advancedcvfilters.advancedcvfilters import AdvancedCVFilters
        if self._properties.get('AdvancedCVFilters', None) is None:
            return AdvancedCVFilters(self)
        else:
            return self._properties.get('AdvancedCVFilters')

    @property
    def AvailableAdvancedFilters(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.availableadvancedfilters.availableadvancedfilters.AvailableAdvancedFilters): An instance of the AvailableAdvancedFilters class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.availableadvancedfilters.availableadvancedfilters import AvailableAdvancedFilters
        if self._properties.get('AvailableAdvancedFilters', None) is None:
            return AvailableAdvancedFilters(self)
        else:
            return self._properties.get('AvailableAdvancedFilters')

    @property
    def AvailablePortFilter(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.availableportfilter.availableportfilter.AvailablePortFilter): An instance of the AvailablePortFilter class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.availableportfilter.availableportfilter import AvailablePortFilter
        if self._properties.get('AvailablePortFilter', None) is None:
            return AvailablePortFilter(self)
        else:
            return self._properties.get('AvailablePortFilter')

    @property
    def AvailableProtocolFilter(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.availableprotocolfilter.availableprotocolfilter.AvailableProtocolFilter): An instance of the AvailableProtocolFilter class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.availableprotocolfilter.availableprotocolfilter import AvailableProtocolFilter
        if self._properties.get('AvailableProtocolFilter', None) is None:
            return AvailableProtocolFilter(self)
        else:
            return self._properties.get('AvailableProtocolFilter')

    @property
    def AvailableProtocolStackFilter(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.availableprotocolstackfilter.availableprotocolstackfilter.AvailableProtocolStackFilter): An instance of the AvailableProtocolStackFilter class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.availableprotocolstackfilter.availableprotocolstackfilter import AvailableProtocolStackFilter
        if self._properties.get('AvailableProtocolStackFilter', None) is None:
            return AvailableProtocolStackFilter(self)
        else:
            return self._properties.get('AvailableProtocolStackFilter')

    @property
    def AvailableStatisticFilter(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.availablestatisticfilter.availablestatisticfilter.AvailableStatisticFilter): An instance of the AvailableStatisticFilter class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.availablestatisticfilter.availablestatisticfilter import AvailableStatisticFilter
        if self._properties.get('AvailableStatisticFilter', None) is None:
            return AvailableStatisticFilter(self)
        else:
            return self._properties.get('AvailableStatisticFilter')

    @property
    def AvailableTrackingFilter(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.availabletrackingfilter.availabletrackingfilter.AvailableTrackingFilter): An instance of the AvailableTrackingFilter class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.availabletrackingfilter.availabletrackingfilter import AvailableTrackingFilter
        if self._properties.get('AvailableTrackingFilter', None) is None:
            return AvailableTrackingFilter(self)
        else:
            return self._properties.get('AvailableTrackingFilter')

    @property
    def AvailableTrafficItemFilter(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.availabletrafficitemfilter.availabletrafficitemfilter.AvailableTrafficItemFilter): An instance of the AvailableTrafficItemFilter class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.availabletrafficitemfilter.availabletrafficitemfilter import AvailableTrafficItemFilter
        if self._properties.get('AvailableTrafficItemFilter', None) is None:
            return AvailableTrafficItemFilter(self)
        else:
            return self._properties.get('AvailableTrafficItemFilter')

    @property
    def Data(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.data.data.Data): An instance of the Data class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.data.data import Data
        if self._properties.get('Data', None) is None:
            return Data(self)._select()
        else:
            return self._properties.get('Data')

    @property
    def DrillDown(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.drilldown.drilldown.DrillDown): An instance of the DrillDown class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.drilldown.drilldown import DrillDown
        if self._properties.get('DrillDown', None) is None:
            return DrillDown(self)
        else:
            return self._properties.get('DrillDown')

    @property
    def FormulaCatalog(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.formulacatalog.formulacatalog.FormulaCatalog): An instance of the FormulaCatalog class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.formulacatalog.formulacatalog import FormulaCatalog
        if self._properties.get('FormulaCatalog', None) is None:
            return FormulaCatalog(self)._select()
        else:
            return self._properties.get('FormulaCatalog')

    @property
    def InnerGlobalStats(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.innerglobalstats.innerglobalstats.InnerGlobalStats): An instance of the InnerGlobalStats class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.innerglobalstats.innerglobalstats import InnerGlobalStats
        if self._properties.get('InnerGlobalStats', None) is None:
            return InnerGlobalStats(self)._select()
        else:
            return self._properties.get('InnerGlobalStats')

    @property
    def Layer23NextGenProtocolFilter(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer23nextgenprotocolfilter.layer23nextgenprotocolfilter.Layer23NextGenProtocolFilter): An instance of the Layer23NextGenProtocolFilter class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer23nextgenprotocolfilter.layer23nextgenprotocolfilter import Layer23NextGenProtocolFilter
        if self._properties.get('Layer23NextGenProtocolFilter', None) is None:
            return Layer23NextGenProtocolFilter(self)
        else:
            return self._properties.get('Layer23NextGenProtocolFilter')

    @property
    def Layer23ProtocolAuthAccessFilter(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer23protocolauthaccessfilter.layer23protocolauthaccessfilter.Layer23ProtocolAuthAccessFilter): An instance of the Layer23ProtocolAuthAccessFilter class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer23protocolauthaccessfilter.layer23protocolauthaccessfilter import Layer23ProtocolAuthAccessFilter
        if self._properties.get('Layer23ProtocolAuthAccessFilter', None) is None:
            return Layer23ProtocolAuthAccessFilter(self)
        else:
            return self._properties.get('Layer23ProtocolAuthAccessFilter')

    @property
    def Layer23ProtocolPortFilter(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer23protocolportfilter.layer23protocolportfilter.Layer23ProtocolPortFilter): An instance of the Layer23ProtocolPortFilter class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer23protocolportfilter.layer23protocolportfilter import Layer23ProtocolPortFilter
        if self._properties.get('Layer23ProtocolPortFilter', None) is None:
            return Layer23ProtocolPortFilter(self)
        else:
            return self._properties.get('Layer23ProtocolPortFilter')

    @property
    def Layer23ProtocolRoutingFilter(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer23protocolroutingfilter.layer23protocolroutingfilter.Layer23ProtocolRoutingFilter): An instance of the Layer23ProtocolRoutingFilter class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer23protocolroutingfilter.layer23protocolroutingfilter import Layer23ProtocolRoutingFilter
        if self._properties.get('Layer23ProtocolRoutingFilter', None) is None:
            return Layer23ProtocolRoutingFilter(self)
        else:
            return self._properties.get('Layer23ProtocolRoutingFilter')

    @property
    def Layer23ProtocolStackFilter(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer23protocolstackfilter.layer23protocolstackfilter.Layer23ProtocolStackFilter): An instance of the Layer23ProtocolStackFilter class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer23protocolstackfilter.layer23protocolstackfilter import Layer23ProtocolStackFilter
        if self._properties.get('Layer23ProtocolStackFilter', None) is None:
            return Layer23ProtocolStackFilter(self)
        else:
            return self._properties.get('Layer23ProtocolStackFilter')

    @property
    def Layer23TrafficFlowDetectiveFilter(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer23trafficflowdetectivefilter.layer23trafficflowdetectivefilter.Layer23TrafficFlowDetectiveFilter): An instance of the Layer23TrafficFlowDetectiveFilter class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer23trafficflowdetectivefilter.layer23trafficflowdetectivefilter import Layer23TrafficFlowDetectiveFilter
        if self._properties.get('Layer23TrafficFlowDetectiveFilter', None) is None:
            return Layer23TrafficFlowDetectiveFilter(self)
        else:
            return self._properties.get('Layer23TrafficFlowDetectiveFilter')

    @property
    def Layer23TrafficFlowFilter(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer23trafficflowfilter.layer23trafficflowfilter.Layer23TrafficFlowFilter): An instance of the Layer23TrafficFlowFilter class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer23trafficflowfilter.layer23trafficflowfilter import Layer23TrafficFlowFilter
        if self._properties.get('Layer23TrafficFlowFilter', None) is None:
            return Layer23TrafficFlowFilter(self)
        else:
            return self._properties.get('Layer23TrafficFlowFilter')

    @property
    def Layer23TrafficItemFilter(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer23trafficitemfilter.layer23trafficitemfilter.Layer23TrafficItemFilter): An instance of the Layer23TrafficItemFilter class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer23trafficitemfilter.layer23trafficitemfilter import Layer23TrafficItemFilter
        if self._properties.get('Layer23TrafficItemFilter', None) is None:
            return Layer23TrafficItemFilter(self)
        else:
            return self._properties.get('Layer23TrafficItemFilter')

    @property
    def Layer23TrafficPortFilter(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer23trafficportfilter.layer23trafficportfilter.Layer23TrafficPortFilter): An instance of the Layer23TrafficPortFilter class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer23trafficportfilter.layer23trafficportfilter import Layer23TrafficPortFilter
        if self._properties.get('Layer23TrafficPortFilter', None) is None:
            return Layer23TrafficPortFilter(self)
        else:
            return self._properties.get('Layer23TrafficPortFilter')

    @property
    def Layer47AppLibraryTrafficFilter(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer47applibrarytrafficfilter.layer47applibrarytrafficfilter.Layer47AppLibraryTrafficFilter): An instance of the Layer47AppLibraryTrafficFilter class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.layer47applibrarytrafficfilter.layer47applibrarytrafficfilter import Layer47AppLibraryTrafficFilter
        if self._properties.get('Layer47AppLibraryTrafficFilter', None) is None:
            return Layer47AppLibraryTrafficFilter(self)
        else:
            return self._properties.get('Layer47AppLibraryTrafficFilter')

    @property
    def Page(self):
        """DEPRECATED 
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.page.page.Page): An instance of the Page class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.page.page import Page
        if self._properties.get('Page', None) is None:
            return Page(self)._select()
        else:
            return self._properties.get('Page')

    @property
    def Statistic(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.statistic.statistic.Statistic): An instance of the Statistic class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.view.statistic.statistic import Statistic
        if self._properties.get('Statistic', None) is None:
            return Statistic(self)
        else:
            return self._properties.get('Statistic')

    @property
    def AutoRefresh(self):
        """DEPRECATED 
        Returns
        -------
        - bool: If true, automatically refreshes the statistics values. Default = true
        """
        return self._get_attribute(self._SDM_ATT_MAP['AutoRefresh'])
    @AutoRefresh.setter
    def AutoRefresh(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AutoRefresh'], value)

    @property
    def AutoUpdate(self):
        """
        Returns
        -------
        - bool: If true, automatically refreshes the statistics values. Default = true
        """
        return self._get_attribute(self._SDM_ATT_MAP['AutoUpdate'])
    @AutoUpdate.setter
    def AutoUpdate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AutoUpdate'], value)

    @property
    def AvailableStatsSelectorColumns(self):
        """
        Returns
        -------
        - list(str): Columns available to be added from Stat Selector Manager
        """
        return self._get_attribute(self._SDM_ATT_MAP['AvailableStatsSelectorColumns'])

    @property
    def Caption(self):
        """
        Returns
        -------
        - str: This is the name that will appear in the GUI stats view window header or in the added view tree from tcl. The caption must be unique.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Caption'])
    @Caption.setter
    def Caption(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Caption'], value)

    @property
    def CsvFileName(self):
        """
        Returns
        -------
        - str: Specifies the file name which is used by the CSV Logging feature. The default value is the caption of the view.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CsvFileName'])
    @CsvFileName.setter
    def CsvFileName(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CsvFileName'], value)

    @property
    def EnableCsvLogging(self):
        """
        Returns
        -------
        - bool: If the CSV Logging feature is enabled the statistics values from a view will be written in a comma separated value format.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableCsvLogging'])
    @EnableCsvLogging.setter
    def EnableCsvLogging(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableCsvLogging'], value)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: If true, enables the view that is created from the tcl script.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def EnabledStatsSelectorColumns(self):
        """
        Returns
        -------
        - list(str): Columns added from Stat Selector Manager
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnabledStatsSelectorColumns'])
    @EnabledStatsSelectorColumns.setter
    def EnabledStatsSelectorColumns(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnabledStatsSelectorColumns'], value)

    @property
    def OnDemandRefreshView(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['OnDemandRefreshView'])

    @property
    def PageTimeout(self):
        """
        Returns
        -------
        - number: The statistics view page is timed out based on the time specified. default = 25,000 ms
        """
        return self._get_attribute(self._SDM_ATT_MAP['PageTimeout'])
    @PageTimeout.setter
    def PageTimeout(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PageTimeout'], value)

    @property
    def ReadOnly(self):
        """
        Returns
        -------
        - bool: The default views created by the application will have this attribute set to false. Tcl SV created by user has this value set to true. Based on this attribute value, the user is allowed to modify the SV attributes.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ReadOnly'])

    @property
    def StatsSelectorManager(self):
        """
        Returns
        -------
        - bool: Flag that denotes whether Stats Selector Manager is enabled for this view or not
        """
        return self._get_attribute(self._SDM_ATT_MAP['StatsSelectorManager'])

    @property
    def TimeSeries(self):
        """
        Returns
        -------
        - bool: If false, then it displays non-timeseries grid views. If true, displays, timeseries line chart view. default = false (non-timeseries)
        """
        return self._get_attribute(self._SDM_ATT_MAP['TimeSeries'])
    @TimeSeries.setter
    def TimeSeries(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TimeSeries'], value)

    @property
    def TreeViewNodeName(self):
        """
        Returns
        -------
        - str: Displays the name of the tree view node.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TreeViewNodeName'])
    @TreeViewNodeName.setter
    def TreeViewNodeName(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TreeViewNodeName'], value)

    @property
    def Type(self):
        """
        Returns
        -------
        - str(layer23NextGenProtocol | layer23ProtocolAuthAccess | layer23ProtocolPort | layer23ProtocolRouting | layer23ProtocolStack | layer23TrafficFlow | layer23TrafficFlowDetective | layer23TrafficItem | layer23TrafficPort | layer47AppLibraryTraffic | sVReadOnly): The type of view the user wants to create from tcl.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Type'])
    @Type.setter
    def Type(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Type'], value)

    @property
    def TypeDescription(self):
        """
        Returns
        -------
        - str: If true, desribes the type
        """
        return self._get_attribute(self._SDM_ATT_MAP['TypeDescription'])

    @property
    def ViewCategory(self):
        """
        Returns
        -------
        - str(ClassicProtocol | L23Traffic | L47Traffic | Mixed | NextGenProtocol | PerSession | Unknown): Returns the category of the view based on the type of statistics displayed by the view.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ViewCategory'])

    @property
    def Visible(self):
        """
        Returns
        -------
        - bool: If true, displays the custom created tcl SVs in the SV tree under TCL Views node.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Visible'])
    @Visible.setter
    def Visible(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Visible'], value)

    def update(self, AutoRefresh=None, AutoUpdate=None, Caption=None, CsvFileName=None, EnableCsvLogging=None, Enabled=None, EnabledStatsSelectorColumns=None, PageTimeout=None, TimeSeries=None, TreeViewNodeName=None, Type=None, Visible=None):
        """Updates view resource on the server.

        Args
        ----
        - AutoRefresh (bool): If true, automatically refreshes the statistics values. Default = true
        - AutoUpdate (bool): If true, automatically refreshes the statistics values. Default = true
        - Caption (str): This is the name that will appear in the GUI stats view window header or in the added view tree from tcl. The caption must be unique.
        - CsvFileName (str): Specifies the file name which is used by the CSV Logging feature. The default value is the caption of the view.
        - EnableCsvLogging (bool): If the CSV Logging feature is enabled the statistics values from a view will be written in a comma separated value format.
        - Enabled (bool): If true, enables the view that is created from the tcl script.
        - EnabledStatsSelectorColumns (list(str)): Columns added from Stat Selector Manager
        - PageTimeout (number): The statistics view page is timed out based on the time specified. default = 25,000 ms
        - TimeSeries (bool): If false, then it displays non-timeseries grid views. If true, displays, timeseries line chart view. default = false (non-timeseries)
        - TreeViewNodeName (str): Displays the name of the tree view node.
        - Type (str(layer23NextGenProtocol | layer23ProtocolAuthAccess | layer23ProtocolPort | layer23ProtocolRouting | layer23ProtocolStack | layer23TrafficFlow | layer23TrafficFlowDetective | layer23TrafficItem | layer23TrafficPort | layer47AppLibraryTraffic | sVReadOnly)): The type of view the user wants to create from tcl.
        - Visible (bool): If true, displays the custom created tcl SVs in the SV tree under TCL Views node.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, AutoRefresh=None, AutoUpdate=None, Caption=None, CsvFileName=None, EnableCsvLogging=None, Enabled=None, EnabledStatsSelectorColumns=None, PageTimeout=None, TimeSeries=None, TreeViewNodeName=None, Type=None, Visible=None):
        """Adds a new view resource on the server and adds it to the container.

        Args
        ----
        - AutoRefresh (bool): If true, automatically refreshes the statistics values. Default = true
        - AutoUpdate (bool): If true, automatically refreshes the statistics values. Default = true
        - Caption (str): This is the name that will appear in the GUI stats view window header or in the added view tree from tcl. The caption must be unique.
        - CsvFileName (str): Specifies the file name which is used by the CSV Logging feature. The default value is the caption of the view.
        - EnableCsvLogging (bool): If the CSV Logging feature is enabled the statistics values from a view will be written in a comma separated value format.
        - Enabled (bool): If true, enables the view that is created from the tcl script.
        - EnabledStatsSelectorColumns (list(str)): Columns added from Stat Selector Manager
        - PageTimeout (number): The statistics view page is timed out based on the time specified. default = 25,000 ms
        - TimeSeries (bool): If false, then it displays non-timeseries grid views. If true, displays, timeseries line chart view. default = false (non-timeseries)
        - TreeViewNodeName (str): Displays the name of the tree view node.
        - Type (str(layer23NextGenProtocol | layer23ProtocolAuthAccess | layer23ProtocolPort | layer23ProtocolRouting | layer23ProtocolStack | layer23TrafficFlow | layer23TrafficFlowDetective | layer23TrafficItem | layer23TrafficPort | layer47AppLibraryTraffic | sVReadOnly)): The type of view the user wants to create from tcl.
        - Visible (bool): If true, displays the custom created tcl SVs in the SV tree under TCL Views node.

        Returns
        -------
        - self: This instance with all currently retrieved view resources using find and the newly added view resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained view resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, AutoRefresh=None, AutoUpdate=None, AvailableStatsSelectorColumns=None, Caption=None, CsvFileName=None, EnableCsvLogging=None, Enabled=None, EnabledStatsSelectorColumns=None, OnDemandRefreshView=None, PageTimeout=None, ReadOnly=None, StatsSelectorManager=None, TimeSeries=None, TreeViewNodeName=None, Type=None, TypeDescription=None, ViewCategory=None, Visible=None):
        """Finds and retrieves view resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve view resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all view resources from the server.

        Args
        ----
        - AutoRefresh (bool): If true, automatically refreshes the statistics values. Default = true
        - AutoUpdate (bool): If true, automatically refreshes the statistics values. Default = true
        - AvailableStatsSelectorColumns (list(str)): Columns available to be added from Stat Selector Manager
        - Caption (str): This is the name that will appear in the GUI stats view window header or in the added view tree from tcl. The caption must be unique.
        - CsvFileName (str): Specifies the file name which is used by the CSV Logging feature. The default value is the caption of the view.
        - EnableCsvLogging (bool): If the CSV Logging feature is enabled the statistics values from a view will be written in a comma separated value format.
        - Enabled (bool): If true, enables the view that is created from the tcl script.
        - EnabledStatsSelectorColumns (list(str)): Columns added from Stat Selector Manager
        - OnDemandRefreshView (bool): 
        - PageTimeout (number): The statistics view page is timed out based on the time specified. default = 25,000 ms
        - ReadOnly (bool): The default views created by the application will have this attribute set to false. Tcl SV created by user has this value set to true. Based on this attribute value, the user is allowed to modify the SV attributes.
        - StatsSelectorManager (bool): Flag that denotes whether Stats Selector Manager is enabled for this view or not
        - TimeSeries (bool): If false, then it displays non-timeseries grid views. If true, displays, timeseries line chart view. default = false (non-timeseries)
        - TreeViewNodeName (str): Displays the name of the tree view node.
        - Type (str(layer23NextGenProtocol | layer23ProtocolAuthAccess | layer23ProtocolPort | layer23ProtocolRouting | layer23ProtocolStack | layer23TrafficFlow | layer23TrafficFlowDetective | layer23TrafficItem | layer23TrafficPort | layer47AppLibraryTraffic | sVReadOnly)): The type of view the user wants to create from tcl.
        - TypeDescription (str): If true, desribes the type
        - ViewCategory (str(ClassicProtocol | L23Traffic | L47Traffic | Mixed | NextGenProtocol | PerSession | Unknown)): Returns the category of the view based on the type of statistics displayed by the view.
        - Visible (bool): If true, displays the custom created tcl SVs in the SV tree under TCL Views node.

        Returns
        -------
        - self: This instance with matching view resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of view data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the view resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def DoDrillDownByOption(self, *args, **kwargs):
        """Executes the doDrillDownByOption operation on the server.

        doDrillDownByOption(Arg2=number, Arg3=string)href
        -------------------------------------------------
        - Arg2 (number): 
        - Arg3 (str): 
        - Returns str(None): 

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('doDrillDownByOption', payload=payload, response_object=None)

    def ExportData(self, *args, **kwargs):
        """Executes the exportData operation on the server.

        Exports the data seen in a view to a file. Supported formats are .html, .xml, .xls and .txt.

        exportData(FilePathName=string)string
        -------------------------------------
        - FilePathName (str): The path where the exported file should be written.
        - Returns str: This can be either a success message or a description of the problem if any error occurred.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('exportData', payload=payload, response_object=None)

    def GetAvailableDrillDownOptions(self, *args, **kwargs):
        """Executes the getAvailableDrillDownOptions operation on the server.

        getAvailableDrillDownOptions(Arg2=number)list
        ---------------------------------------------
        - Arg2 (number): 
        - Returns list(str): 

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('getAvailableDrillDownOptions', payload=payload, response_object=None)

    def GetColumnValues(self, *args, **kwargs):
        """Executes the getColumnValues operation on the server.

        Retrieves the requested column values.

        getColumnValues(Arg2=string)object
        ----------------------------------
        - Arg2 (str): The name of the column for which to retrieve statistics.
        - Returns dict(arg1:list[str],arg2:str): An array with the values retrieved.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('getColumnValues', payload=payload, response_object=None)

    def GetResultsPath(self):
        """Executes the getResultsPath operation on the server.

        Gets the path where the results for the current tests are stored.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('getResultsPath', payload=payload, response_object=None)

    def GetRowValues(self, *args, **kwargs):
        """Executes the getRowValues operation on the server.

        Retrieves the requested row values.

        getRowValues(Arg2=string)object
        -------------------------------
        - Arg2 (str): The label identifying the row for which to retrieve statistics. It is formed from the values of the row label columns concatenated using | delimiter. Row label columns appear with orange or yellow names in the view.
        - Returns dict(arg1:list[str],arg2:str): An array with the values retrieved.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('getRowValues', payload=payload, response_object=None)

    def GetValue(self, *args, **kwargs):
        """Executes the getValue operation on the server.

        Retrieves the requested statistical data.

        getValue(Arg2=string, Arg3=string)string
        ----------------------------------------
        - Arg2 (str): The label identifying the row for which to retrieve statistics. It is formed from the values of the row label columns concatenated using | delimiter. Row label columns appear with orange or yellow names in the view.
        - Arg3 (str): The name of the column for which to retrieve statistics.
        - Returns str: The retrieved value.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('getValue', payload=payload, response_object=None)

    def Refresh(self):
        """Executes the refresh operation on the server.

        Refreshes the existing values in the view with the new values. If the view is NGPF on demand, the refresh will get new values for all NGPF on demand views.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('refresh', payload=payload, response_object=None)

    def RestoreToDefaults(self):
        """Executes the restoreToDefaults operation on the server.

        NOT DEFINED

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('restoreToDefaults', payload=payload, response_object=None)

    def SetEgressViewMode(self, *args, **kwargs):
        """Executes the setEgressViewMode operation on the server.

        setEgressViewMode(Arg2=enum)number
        ----------------------------------
        - Arg2 (str(kAll | kRowsWithNoPackets | kRowsWithPackets)): 
        - Returns number: 

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('setEgressViewMode', payload=payload, response_object=None)
