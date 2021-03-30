from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Ethernet_RARP(Base):
    __slots__ = ()
    _SDM_NAME = 'ethernetRARP'
    _SDM_ATT_MAP = {
        'Hardware Type': 'ethernetRARP.header.hwType',
        'Protocol Type': 'ethernetRARP.header.protocolType',
        'Hardware Address Length': 'ethernetRARP.header.hwAddressLength',
        'Protocol Address Length': 'ethernetRARP.header.protocolAddressLength',
        'Op Code': 'ethernetRARP.header.opCode',
        'Sender Hardware Address': 'ethernetRARP.header.srcHwAddr',
        'Sender Protocol Address': 'ethernetRARP.header.srcIp',
        'Target Hardware Address': 'ethernetRARP.header.dstHwAddr',
        'Target Protocol Address': 'ethernetRARP.header.dstIp',
    }

    def __init__(self, parent):
        super(Ethernet_RARP, self).__init__(parent)

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
