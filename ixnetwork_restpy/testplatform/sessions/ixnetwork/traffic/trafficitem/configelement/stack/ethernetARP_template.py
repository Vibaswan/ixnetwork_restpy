from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Ethernet_ARP(Base):
    __slots__ = ()
    _SDM_NAME = 'ethernetARP'
    _SDM_ATT_MAP = {
        'Hardware Type': 'ethernetARP.header.hardwareType',
        'Protocol Type': 'ethernetARP.header.protocolType',
        'Hardware Address Length': 'ethernetARP.header.hardwareAddressLength',
        'Protocol Address Length': 'ethernetARP.header.protocolAddressLength',
        'Op Code': 'ethernetARP.header.opCode',
        'Sender Hardware Address': 'ethernetARP.header.srcHardwareAddress',
        'Sender Protocol Address': 'ethernetARP.header.srcIP',
        'Target Hardware Address': 'ethernetARP.header.dstHardwareAddress',
        'Target Protocol Address': 'ethernetARP.header.dstIP',
    }

    def __init__(self, parent):
        super(Ethernet_ARP, self).__init__(parent)

    @property
    def Hardware_Type(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Hardware Type']))

    @property
    def Protocol_Type(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Protocol Type']))

    @property
    def Hardware_Address_Length(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Hardware Address Length']))

    @property
    def Protocol_Address_Length(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Protocol Address Length']))

    @property
    def Op_Code(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Op Code']))

    @property
    def Sender_Hardware_Address(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Sender Hardware Address']))

    @property
    def Sender_Protocol_Address(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Sender Protocol Address']))

    @property
    def Target_Hardware_Address(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Target Hardware Address']))

    @property
    def Target_Protocol_Address(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Target Protocol Address']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
