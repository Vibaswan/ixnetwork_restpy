from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class LISP_Map_Request(Base):
    __slots__ = ()
    _SDM_NAME = 'lISPMapRequest'
    _SDM_ATT_MAP = {
        'Type': 'lISPMapRequest.header.type',
        'A': 'lISPMapRequest.header.a',
        'M': 'lISPMapRequest.header.M',
        'P': 'lISPMapRequest.header.p',
        'S': 'lISPMapRequest.header.S',
        'Reserved': 'lISPMapRequest.header.reserved',
        'IRC': 'lISPMapRequest.header.IRC_RLOC_Count',
        'Record Count': 'lISPMapRequest.header.recordcount',
        'Nonce': 'lISPMapRequest.header.nonce',
        'Source EID AFI/Address': 'lISPMapRequest.header.Source_EID_AFI_Address',
        'ITR-RLOC AFI/Address': 'lISPMapRequest.header.ITR_RLOC_AFI_Address',
        'EID Record': 'lISPMapRequest.header.EID Record',
        'Map-Reply Record': 'lISPMapRequest.header.Map-Reply Record',
        'Mapping Protocol Data': 'lISPMapRequest.header.Mapping_Protocol_Data',
    }

    def __init__(self, parent):
        super(LISP_Map_Request, self).__init__(parent)

    @property
    def Type(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Type']))

    @property
    def A(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['A']))

    @property
    def M(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['M']))

    @property
    def P(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['P']))

    @property
    def S(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['S']))

    @property
    def Reserved(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Reserved']))

    @property
    def IRC(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['IRC']))

    @property
    def Record_Count(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Record Count']))

    @property
    def Nonce(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Nonce']))

    @property
    def Source_EID_AFI_Address(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Source EID AFI/Address']))

    @property
    def ITR_RLOC_AFI_Address(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ITR-RLOC AFI/Address']))

    @property
    def EID_Record(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EID Record']))

    @property
    def Map_Reply_Record(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Map-Reply Record']))

    @property
    def Mapping_Protocol_Data(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Mapping Protocol Data']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
