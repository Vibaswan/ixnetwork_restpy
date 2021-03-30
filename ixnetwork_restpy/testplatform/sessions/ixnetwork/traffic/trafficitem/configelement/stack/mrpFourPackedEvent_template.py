from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class MRP_Four_Packed_Event(Base):
    __slots__ = ()
    _SDM_NAME = 'mrpFourPackedEvent'
    _SDM_ATT_MAP = {
        'Four Packed Attribute Event': 'mrpFourPackedEvent.header.fourPackedAttributeEvent',
    }

    def __init__(self, parent):
        super(MRP_Four_Packed_Event, self).__init__(parent)

    @property
    def Four_Packed_Attribute_Event(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Four Packed Attribute Event']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
