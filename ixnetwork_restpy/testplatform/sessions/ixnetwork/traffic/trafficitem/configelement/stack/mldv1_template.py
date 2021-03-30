from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class MLDv1(Base):
    __slots__ = ()
    _SDM_NAME = 'mldv1'
    _SDM_ATT_MAP = {
        'Type': 'mldv1 .header.type',
        'Code': 'mldv1 .header.code',
        'MLDv1 checksum': 'mldv1 .header.mldv1Checksum',
        'Maximum response delay': 'mldv1 .header.maximumResponseDelay',
        'Reserved': 'mldv1 .header.reserved',
        'Multicast address': 'mldv1 .header.multicastAddress',
    }

    def __init__(self, parent):
        super(MLDv1, self).__init__(parent)

    @property
    def Type(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Type']))

    @property
    def Code(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Code']))

    @property
    def MLDv1_checksum(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MLDv1 checksum']))

    @property
    def Maximum_response_delay(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Maximum response delay']))

    @property
    def Reserved(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Reserved']))

    @property
    def Multicast_address(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Multicast address']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
