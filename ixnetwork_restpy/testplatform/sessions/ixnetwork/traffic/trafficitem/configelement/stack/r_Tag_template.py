from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class R_Tag(Base):
    __slots__ = ()
    _SDM_NAME = 'r_Tag'
    _SDM_ATT_MAP = {
        'Reserved': 'rTag.rTag.RTagReserved',
        'Sequence Number': 'rTag.rTag.RTagSeqNum',
        'Ethernet-Type': 'rTag.rTag.rtagEtherType',
    }

    def __init__(self, parent):
        super(R_Tag, self).__init__(parent)

    @property
    def Reserved(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Reserved']))

    @property
    def Sequence_Number(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Sequence Number']))

    @property
    def Ethernet_Type(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Ethernet-Type']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
