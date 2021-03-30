from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class GTPu_Optional_Fields(Base):
    __slots__ = ()
    _SDM_NAME = 'gTPuOptionalFields'
    _SDM_ATT_MAP = {
        'Sequence Number': 'gTPuOptionalFields.header.sequenceNumber',
        'N-PDU Number': 'gTPuOptionalFields.header.npduNumber',
        'Next Extension Header Field': 'gTPuOptionalFields.header.nextExtHdrField',
        'Next Extension Headers': 'gTPuOptionalFields.header.nextExtHdrs',
    }

    def __init__(self, parent):
        super(GTPu_Optional_Fields, self).__init__(parent)

    @property
    def Sequence_Number(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Sequence Number']))

    @property
    def N_PDU_Number(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['N-PDU Number']))

    @property
    def Next_Extension_Header_Field(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Next Extension Header Field']))

    @property
    def Next_Extension_Headers(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Next Extension Headers']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
