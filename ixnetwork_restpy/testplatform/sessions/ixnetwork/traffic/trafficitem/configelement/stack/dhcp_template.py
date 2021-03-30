from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class DHCP(Base):
    __slots__ = ()
    _SDM_NAME = 'dhcp'
    _SDM_ATT_MAP = {
        'Message op code': 'dhcp.header.opCode',
        'Hardware type': 'dhcp.header.hwType',
        'Hardware address length (bytes)': 'dhcp.header.hwAddressLen',
        'Hops': 'dhcp.header.hops',
        'Transaction ID': 'dhcp.header.transactionId',
        'Seconds elapsed': 'dhcp.header.secondsElapsed',
        'Broadcast flag': 'dhcp.header.broadcastFlag',
        'Client IP address': 'dhcp.header.clientIP',
        'Your IP address': 'dhcp.header.yourIP',
        'Server IP address': 'dhcp.header.serverIP',
        'Relay agent IP address': 'dhcp.header.relayAgentIP',
        'Client hardware address': 'dhcp.header.clientHwAddress',
        'Optional server hostname': 'dhcp.header.optionalServerName',
        'Boot file name': 'dhcp.header.bootFile',
        'DHCP options / BOOTP vendor': 'dhcp.header.options',
    }

    def __init__(self, parent):
        super(DHCP, self).__init__(parent)

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
