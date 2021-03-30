from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class L2TPv2_Control_Message(Base):
    __slots__ = ()
    _SDM_NAME = 'l2TPv2Control'
    _SDM_ATT_MAP = {
        'L2TPv2 Control Message Header': 'l2TPv2Control.header.controlHeader',
        'Message type Attribute-Value Pair': 'l2TPv2Control.header.messageTypeAvp',
        'Next AVP': 'l2TPv2Control.header.nextAvp',
    }

    def __init__(self, parent):
        super(L2TPv2_Control_Message, self).__init__(parent)

    @property
    def L2TPv2_Control_Message_Header(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['L2TPv2 Control Message Header']))

    @property
    def Message_type_Attribute_Value_Pair(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Message type Attribute-Value Pair']))

    @property
    def Next_AVP(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Next AVP']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
