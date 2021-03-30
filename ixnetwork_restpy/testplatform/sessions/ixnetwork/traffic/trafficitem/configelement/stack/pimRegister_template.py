from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class PIM_Register_Message(Base):
    __slots__ = ()
    _SDM_NAME = 'pimRegister'
    _SDM_ATT_MAP = {
        'Version': 'pimRegister.header.version',
        'Message type': 'pimRegister.header.messageType',
        'Reserved': 'pimRegister.header.reserved',
        'Checksum': 'pimRegister.header.checksum',
        'Border Bit': 'pimRegister.header.borderBit',
        'Null Register Bit': 'pimRegister.header.nullRegisterBit',
        'Reserved2': 'pimRegister.header.reserved2',
    }

    def __init__(self, parent):
        super(PIM_Register_Message, self).__init__(parent)

    @property
    def Version(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Version']))

    @property
    def Message_type(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Message type']))

    @property
    def Reserved(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Reserved']))

    @property
    def Checksum(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Checksum']))

    @property
    def Border_Bit(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Border Bit']))

    @property
    def Null_Register_Bit(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Null Register Bit']))

    @property
    def Reserved2(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Reserved2']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
