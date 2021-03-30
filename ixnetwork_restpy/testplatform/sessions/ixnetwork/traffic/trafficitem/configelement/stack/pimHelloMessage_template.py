from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class PIM_Hello_Message(Base):
    __slots__ = ()
    _SDM_NAME = 'pimHelloMessage'
    _SDM_ATT_MAP = {
        'Version': 'pimHelloMessage.header.version',
        'Type': 'pimHelloMessage.header.type',
        'Reserved': 'pimHelloMessage.header.reserved',
        'Header checksum': 'pimHelloMessage.header.headerChecksum',
        'Hello Options Fields': 'pimHelloMessage.header.helloOptionsFields',
    }

    def __init__(self, parent):
        super(PIM_Hello_Message, self).__init__(parent)

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
    def Header_checksum(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Header checksum']))

    @property
    def Hello_Options_Fields(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Hello Options Fields']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
