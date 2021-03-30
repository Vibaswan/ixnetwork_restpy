from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Minimal_IP(Base):
    __slots__ = ()
    _SDM_NAME = 'minimalIP'
    _SDM_ATT_MAP = {
        'Protocol': 'minimalIP.minimalEncapsulationHeader.protocol',
        'S bit': 'minimalIP.minimalEncapsulationHeader.sBit',
        'Reserved': 'minimalIP.minimalEncapsulationHeader.reserved',
        'Checksum': 'minimalIP.minimalEncapsulationHeader.checksum',
        'Original Destination Address': 'minimalIP.minimalEncapsulationHeader.originalDestinationAddress',
        'Source Option': 'minimalIP.minimalEncapsulationHeader.sourceOption',
    }

    def __init__(self, parent):
        super(Minimal_IP, self).__init__(parent)

    @property
    def Protocol(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Protocol']))

    @property
    def S_bit(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['S bit']))

    @property
    def Reserved(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Reserved']))

    @property
    def Checksum(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Checksum']))

    @property
    def Original_Destination_Address(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Original Destination Address']))

    @property
    def Source_Option(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Source Option']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
