from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class PIM_Register_Stop_Message(Base):
    __slots__ = ()
    _SDM_NAME = 'pimRegisterStopMessage'
    _SDM_ATT_MAP = {
        'Version': 'pimRegisterStopMessage.header.version',
        'Type': 'pimRegisterStopMessage.header.type',
        'Reserved': 'pimRegisterStopMessage.header.reserved',
        'Checksum': 'pimRegisterStopMessage.header.checksum',
        'Encoded Grp Address': 'pimRegisterStopMessage.header.encodedGrpAddress',
        'Encoded Ucast Src Address': 'pimRegisterStopMessage.header.encodedUcastSrcAddress',
    }

    def __init__(self, parent):
        super(PIM_Register_Stop_Message, self).__init__(parent)

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
    def Checksum(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Checksum']))

    @property
    def Encoded_Grp_Address(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Encoded Grp Address']))

    @property
    def Encoded_Ucast_Src_Address(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Encoded Ucast Src Address']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
