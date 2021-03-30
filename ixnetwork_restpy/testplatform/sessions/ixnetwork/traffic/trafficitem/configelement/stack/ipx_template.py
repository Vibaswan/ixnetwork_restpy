from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class IPX(Base):
    __slots__ = ()
    _SDM_NAME = 'ipx'
    _SDM_ATT_MAP = {
        'Checksum': 'ipx.header.checksum',
        'Packet length': 'ipx.header.length',
        'Transport control': 'ipx.header.transportControl',
        'Packet type': 'ipx.header.type',
        'Destination network': 'ipx.header.dstNetwork',
        'Destination node': 'ipx.header.dstNode',
        'Destination socket': 'ipx.header.dstSocket',
        'Source network': 'ipx.header.srcNetwork',
        'Source node': 'ipx.header.srcNode',
        'Source socket': 'ipx.header.srcSocket',
    }

    def __init__(self, parent):
        super(IPX, self).__init__(parent)

    @property
    def Checksum(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Checksum']))

    @property
    def Packet_length(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Packet length']))

    @property
    def Transport_control(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Transport control']))

    @property
    def Packet_type(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Packet type']))

    @property
    def Destination_network(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Destination network']))

    @property
    def Destination_node(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Destination node']))

    @property
    def Destination_socket(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Destination socket']))

    @property
    def Source_network(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Source network']))

    @property
    def Source_node(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Source node']))

    @property
    def Source_socket(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Source socket']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
