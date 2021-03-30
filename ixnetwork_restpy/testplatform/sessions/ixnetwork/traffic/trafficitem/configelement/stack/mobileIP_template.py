from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Mobile_IP(Base):
    __slots__ = ()
    _SDM_NAME = 'mobileIP'
    _SDM_ATT_MAP = {
        'Mobile IP Packet Type': 'mobileIP.header.packetType',
    }

    def __init__(self, parent):
        super(Mobile_IP, self).__init__(parent)

    @property
    def Mobile_IP_Packet_Type(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Mobile IP Packet Type']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
