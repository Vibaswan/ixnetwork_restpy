from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class MPLS(Base):
    __slots__ = ()
    _SDM_NAME = 'mpls'
    _SDM_ATT_MAP = {
        'Label Value': 'mpls.label.value',
        'MPLS Exp': 'mpls.label.experimental',
        'Bottom of Stack Bit': 'mpls.label.bottomOfStack',
        'Time To Live': 'mpls.label.ttl',
        'Label Tracker': 'mpls.label.tracker',
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

    @property
    def Label_Tracker(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Label Tracker']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
