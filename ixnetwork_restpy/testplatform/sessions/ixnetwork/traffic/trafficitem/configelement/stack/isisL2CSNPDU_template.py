from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class IS_IS_Level_2_Complete_Sequence_Number_PDU(Base):
    __slots__ = ()
    _SDM_NAME = 'isisL2CSNPDU'
    _SDM_ATT_MAP = {
        'Common header': 'isisL2CSNPDU.isisHeader.commonHeader',
        'Fixed header': 'isisL2CSNPDU.isisHeader.fixedHeader',
        'TLV header': 'isisL2CSNPDU.isisHeader.tlvHeader',
    }

    def __init__(self, parent):
        super(IS_IS_Level_2_Complete_Sequence_Number_PDU, self).__init__(parent)

    @property
    def Common_header(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Common header']))

    @property
    def Fixed_header(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Fixed header']))

    @property
    def TLV_header(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TLV header']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
