from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class LISP_Encapsulated_Control_Message(Base):
    __slots__ = ()
    _SDM_NAME = 'lISPEncapsulatedControlMessage'
    _SDM_ATT_MAP = {
        'Type': 'lISPEncapsulatedControlMessage.header.type',
        'Reserved': 'lISPEncapsulatedControlMessage.header.reserved',
    }

    def __init__(self, parent):
        super(LISP_Encapsulated_Control_Message, self).__init__(parent)

    @property
    def Type(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Type']))

    @property
    def Reserved(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Reserved']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
