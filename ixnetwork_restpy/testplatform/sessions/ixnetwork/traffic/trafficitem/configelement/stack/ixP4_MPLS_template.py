from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class IxP4_MPLS(Base):
    __slots__ = ()
    _SDM_NAME = 'ixP4_MPLS'
    _SDM_ATT_MAP = {
        'label': 'ixP4_MPLS.mPLS.label',
        'exp': 'ixP4_MPLS.mPLS.exp',
        'bos': 'ixP4_MPLS.mPLS.bos',
        'ttl': 'ixP4_MPLS.mPLS.ttl',
    }

    def __init__(self, parent):
        super(IxP4_MPLS, self).__init__(parent)

    @property
    def label(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['label']))

    @property
    def exp(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['exp']))

    @property
    def bos(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['bos']))

    @property
    def ttl(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ttl']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
