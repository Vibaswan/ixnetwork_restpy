from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class MPLS(Base):
    __slots__ = ()
    _SDM_NAME = 'mpls_enull'
    _SDM_ATT_MAP = {
        'Label Value': 'mpls_enull.label.value',
        'MPLS Exp': 'mpls_enull.label.experimental',
        'Bottom of Stack Bit': 'mpls_enull.label.bottomOfStack',
        'Time To Live': 'mpls_enull.label.ttl',
    }

    def __init__(self, parent):
        super(MPLS, self).__init__(parent)

    @property
    def Label_Value(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Label Value']))

    @property
    def MPLS_Exp(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MPLS Exp']))

    @property
    def Bottom_of_Stack_Bit(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Bottom of Stack Bit']))

    @property
    def Time_To_Live(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Time To Live']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
