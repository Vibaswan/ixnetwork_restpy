from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class LISP_Map_Reply(Base):
    __slots__ = ()
    _SDM_NAME = 'lISPMapReply'
    _SDM_ATT_MAP = {
        'Type': 'lISPMapReply.header.type',
        'P': 'lISPMapReply.header.p',
        'E': 'lISPMapReply.header.E',
        'Reserved': 'lISPMapReply.header.reserved',
        'Record Count': 'lISPMapReply.header.recordcount',
        'Nonce': 'lISPMapReply.header.nonce',
        'EID Record': 'lISPMapReply.header.eidrecord',
        'Mapping Protocol Data': 'lISPMapReply.header.Mapping_Protocol_Data',
    }

    def __init__(self, parent):
        super(LISP_Map_Reply, self).__init__(parent)

    @property
    def Type(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Type']))

    @property
    def P(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['P']))

    @property
    def E(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['E']))

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
    def EID_Record(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EID Record']))

    @property
    def Mapping_Protocol_Data(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Mapping Protocol Data']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
