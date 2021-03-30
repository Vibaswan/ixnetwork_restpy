from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class IS_IS_Level_2_Link_State_PDU(Base):
    __slots__ = ()
    _SDM_NAME = 'isisLevel2LinkStatePDU'
    _SDM_ATT_MAP = {
        'Common header': 'isisLevel2LinkStatePDU.isisHeader.commonHeader',
        'Fixed header': 'isisLevel2LinkStatePDU.isisHeader.fixedHeader',
        'TLV header': 'isisLevel2LinkStatePDU.isisHeader.tlvHeader',
    }

    def __init__(self, parent):
        super(IS_IS_Level_2_Link_State_PDU, self).__init__(parent)

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
