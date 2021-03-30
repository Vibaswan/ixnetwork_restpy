from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class GTPu(Base):
    __slots__ = ()
    _SDM_NAME = 'gtpu'
    _SDM_ATT_MAP = {
        'Version': 'gtpu.header.version',
        'PT': 'gtpu.header.pt',
        'Reserved': 'gtpu.header.reserved',
        'E': 'gtpu.header.e',
        'S': 'gtpu.header.s',
        'N': 'gtpu.header.n',
        'Type': 'gtpu.header.type',
        'Total Length': 'gtpu.header.totalLength',
        'TEID': 'gtpu.header.teid',
    }

    def __init__(self, parent):
        super(GTPu, self).__init__(parent)

    @property
    def Version(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Version']))

    @property
    def PT(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PT']))

    @property
    def Reserved(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Reserved']))

    @property
    def E(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['E']))

    @property
    def S(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['S']))

    @property
    def N(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['N']))

    @property
    def Type(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Type']))

    @property
    def Total_Length(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Total Length']))

    @property
    def TEID(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TEID']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
