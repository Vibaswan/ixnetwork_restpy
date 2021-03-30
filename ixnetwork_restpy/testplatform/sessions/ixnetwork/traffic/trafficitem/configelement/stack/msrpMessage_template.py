from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class MSRP_Message(Base):
    __slots__ = ()
    _SDM_NAME = 'msrpMessage'
    _SDM_ATT_MAP = {
        'MSR PDU': 'msrpMessage.header.msrpHeader',
        'Select Attribute Type': 'msrpMessage.header.attributeType',
        'Attribute List Length': 'msrpMessage.header.attributeListLength',
    }

    def __init__(self, parent):
        super(MSRP_Message, self).__init__(parent)

    @property
    def MSR_PDU(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MSR PDU']))

    @property
    def Select_Attribute_Type(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Select Attribute Type']))

    @property
    def Attribute_List_Length(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Attribute List Length']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
