from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class LISP_Map_Register(Base):
    __slots__ = ()
    _SDM_NAME = 'lISPMapRegister'
    _SDM_ATT_MAP = {
        'Type': 'lISPMapRegister.header.type',
        'P': 'lISPMapRegister.header.p',
        'Reserved': 'lISPMapRegister.header.reserved',
        'M': 'lISPMapRegister.header.m',
        'Record Count': 'lISPMapRegister.header.recordcount',
        'Nonce': 'lISPMapRegister.header.nonce',
        'Key ID': 'lISPMapRegister.header.keyid',
        'Auth Data Length': 'lISPMapRegister.header.authdatalen',
        'Auth Data': 'lISPMapRegister.header.authdata',
        'Record': 'lISPMapRegister.header.eidrecord',
    }

    def __init__(self, parent):
        super(LISP_Map_Register, self).__init__(parent)

    @property
    def Type(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Type']))

    @property
    def P(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['P']))

    @property
    def Reserved(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Reserved']))

    @property
    def M(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['M']))

    @property
    def Record_Count(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Record Count']))

    @property
    def Nonce(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Nonce']))

    @property
    def Key_ID(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Key ID']))

    @property
    def Auth_Data_Length(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Auth Data Length']))

    @property
    def Auth_Data(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Auth Data']))

    @property
    def Record(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Record']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
