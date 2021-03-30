from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class I_Tag_Header(Base):
    __slots__ = ()
    _SDM_NAME = 'iTagHeader'
    _SDM_ATT_MAP = {
        'Ethertype value': 'iTagHeader.iTAGEthertype.ethertypeValue',
        'I-TAG': 'iTagHeader.iTAGEthertype.iTAG',
    }

    def __init__(self, parent):
        super(I_Tag_Header, self).__init__(parent)

    @property
    def Ethertype_value(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Ethertype value']))

    @property
    def I_TAG(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['I-TAG']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
