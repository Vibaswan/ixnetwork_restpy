from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class MMRP_Message(Base):
    __slots__ = ()
    _SDM_NAME = 'mmrpMessage'
    _SDM_ATT_MAP = {
        'MMRP PDU': 'mmrpMessage.header.mmrpHeader',
        'Select Attribute Type': 'mmrpMessage.header.attributeType',
    }

    def __init__(self, parent):
        super(MMRP_Message, self).__init__(parent)

    @property
    def MMRP_PDU(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MMRP PDU']))

    @property
    def Select_Attribute_Type(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Select Attribute Type']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
