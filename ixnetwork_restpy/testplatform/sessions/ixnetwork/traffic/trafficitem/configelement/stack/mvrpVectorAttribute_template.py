from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class MVRP_Vector_Attribute(Base):
    __slots__ = ()
    _SDM_NAME = 'mvrpVectorAttribute'
    _SDM_ATT_MAP = {
        'Vector Header': 'mvrpVectorAttribute.header.vectorHeader',
        'Select First Value Type': 'mvrpVectorAttribute.header.selectFirstValueType',
    }

    def __init__(self, parent):
        super(MVRP_Vector_Attribute, self).__init__(parent)

    @property
    def Vector_Header(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Vector Header']))

    @property
    def Select_First_Value_Type(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Select First Value Type']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
