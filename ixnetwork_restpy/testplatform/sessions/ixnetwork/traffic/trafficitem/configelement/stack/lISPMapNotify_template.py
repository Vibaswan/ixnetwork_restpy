from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class LISP_Map_Notify(Base):
    __slots__ = ()
    _SDM_NAME = 'lISPMapNotify'
    _SDM_ATT_MAP = {
        'Type': 'lISPMapNotify.header.type',
        'Reserved': 'lISPMapNotify.header.reserved',
        'Record Count': 'lISPMapNotify.header.recordcount',
        'Nonce': 'lISPMapNotify.header.nonce',
        'Key ID': 'lISPMapNotify.header.keyid',
        'Auth Data Length': 'lISPMapNotify.header.authdatalen',
        'Auth Data': 'lISPMapNotify.header.authdata',
        'Record': 'lISPMapNotify.header.eidrecord',
    }

    def __init__(self, parent):
        super(LISP_Map_Notify, self).__init__(parent)

    @property
    def Type(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Type']))

    @property
    def Reserved(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Reserved']))

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
