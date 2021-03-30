from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Mobile_IPv6(Base):
    __slots__ = ()
    _SDM_NAME = 'mobileIPv6'
    _SDM_ATT_MAP = {
        'Payload Protocol': 'mobileIPv6.mobileIPv6Packet.protocol',
        'Header Length': 'mobileIPv6.mobileIPv6Packet.length',
        'MH Type': 'mobileIPv6.mobileIPv6Packet.mhType',
        'Reserved': 'mobileIPv6.mobileIPv6Packet.reserved',
        'Checksum': 'mobileIPv6.mobileIPv6Packet.checksum',
        'Message Body': 'mobileIPv6.mobileIPv6Packet.body',
        'Message Options Holder': 'mobileIPv6.mobileIPv6Packet.optionsHolder',
    }

    def __init__(self, parent):
        super(Mobile_IPv6, self).__init__(parent)

    @property
    def Payload_Protocol(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Payload Protocol']))

    @property
    def Header_Length(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Header Length']))

    @property
    def MH_Type(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MH Type']))

    @property
    def Reserved(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Reserved']))

    @property
    def Checksum(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Checksum']))

    @property
    def Message_Body(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Message Body']))

    @property
    def Message_Options_Holder(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Message Options Holder']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
