from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class BIER(Base):
    __slots__ = ()
    _SDM_NAME = 'bier'
    _SDM_ATT_MAP = {
        'Nibble': 'bier.header.nibble',
        'Ver': 'bier.header.ver',
        'BSL': 'bier.header.bsl',
        'Entropy': 'bier.header.entropy',
        'OAM': 'bier.header.oam',
        'Rsv': 'bier.header.rsv',
        'DSCP': 'bier.header.dscp',
        'Proto': 'bier.header.proto',
        'BFIR-Id': 'bier.header.bfirId',
        'BitString': 'bier.header.bitString',
    }

    def __init__(self, parent):
        super(BIER, self).__init__(parent)

    @property
    def Nibble(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Nibble']))

    @property
    def Ver(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Ver']))

    @property
    def BSL(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BSL']))

    @property
    def Entropy(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Entropy']))

    @property
    def OAM(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['OAM']))

    @property
    def Rsv(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Rsv']))

    @property
    def DSCP(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DSCP']))

    @property
    def Proto(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Proto']))

    @property
    def BFIR_Id(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BFIR-Id']))

    @property
    def BitString(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BitString']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
