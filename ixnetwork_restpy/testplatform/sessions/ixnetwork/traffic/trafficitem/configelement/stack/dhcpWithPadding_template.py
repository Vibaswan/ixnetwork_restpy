from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class DHCP_With_Padding(Base):
    __slots__ = ()
    _SDM_NAME = 'dhcpWithPadding'
    _SDM_ATT_MAP = {
        'Message op code': 'dhcpWithPadding.header.opCode',
        'Hardware type': 'dhcpWithPadding.header.hwType',
        'Hardware address length (bytes)': 'dhcpWithPadding.header.hwAddressLen',
        'Hops': 'dhcpWithPadding.header.hops',
        'Transaction ID': 'dhcpWithPadding.header.transactionId',
        'Seconds elapsed': 'dhcpWithPadding.header.secondsElapsed',
        'Broadcast flag': 'dhcpWithPadding.header.broadcastFlag',
        'Client IP address': 'dhcpWithPadding.header.clientIP',
        'Your IP address': 'dhcpWithPadding.header.yourIP',
        'Server IP address': 'dhcpWithPadding.header.serverIP',
        'Relay agent IP address': 'dhcpWithPadding.header.relayAgentIP',
        'Client hardware address': 'dhcpWithPadding.header.clientHwAddress',
        'Client hardware address padding': 'dhcpWithPadding.header.clientHwAddressPad',
        'Optional server hostname': 'dhcpWithPadding.header.optionalServerName',
        'Boot file name': 'dhcpWithPadding.header.bootFile',
        'DHCP options / BOOTP vendor': 'dhcpWithPadding.header.options',
    }

    def __init__(self, parent):
        super(DHCP_With_Padding, self).__init__(parent)

    @property
    def Message_op_code(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Message op code']))

    @property
    def Hardware_type(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Hardware type']))

    @property
    def Hardware_address_length_bytes(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Hardware address length (bytes)']))

    @property
    def Hops(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Hops']))

    @property
    def Transaction_ID(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Transaction ID']))

    @property
    def Seconds_elapsed(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Seconds elapsed']))

    @property
    def Broadcast_flag(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Broadcast flag']))

    @property
    def Client_IP_address(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Client IP address']))

    @property
    def Your_IP_address(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Your IP address']))

    @property
    def Server_IP_address(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Server IP address']))

    @property
    def Relay_agent_IP_address(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Relay agent IP address']))

    @property
    def Client_hardware_address(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Client hardware address']))

    @property
    def Client_hardware_address_padding(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Client hardware address padding']))

    @property
    def Optional_server_hostname(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Optional server hostname']))

    @property
    def Boot_file_name(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Boot file name']))

    @property
    def DHCP_options___BOOTP_vendor(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DHCP options / BOOTP vendor']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
