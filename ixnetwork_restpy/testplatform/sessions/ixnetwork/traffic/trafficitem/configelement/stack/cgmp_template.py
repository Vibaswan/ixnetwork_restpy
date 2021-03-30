from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class CGMP(Base):
    __slots__ = ()
    _SDM_NAME = 'cgmp'
    _SDM_ATT_MAP = {
        'Version': 'cgmp.header.version',
        'Type': 'cgmp.header.type',
        'Reserved': 'cgmp.header.reserved',
        'Count': 'cgmp.header.count',
        'Address Set': 'cgmp.header.addressSet',
    }

    def __init__(self, parent):
        super(CGMP, self).__init__(parent)

    @property
    def Version(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Version']))

    @property
    def Type(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Type']))

    @property
    def Reserved(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Reserved']))

    @property
    def Count(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Count']))

    @property
    def Address_Set(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Address Set']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
