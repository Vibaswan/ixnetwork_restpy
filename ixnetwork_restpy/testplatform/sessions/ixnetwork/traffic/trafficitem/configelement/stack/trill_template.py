from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class TRILL(Base):
    __slots__ = ()
    _SDM_NAME = 'trill'
    _SDM_ATT_MAP = {
        'Version': 'trill.trillHeader.ver',
        'Reserved': 'trill.trillHeader.res',
        'Multi Destination': 'trill.trillHeader.multdest',
        'Options Length': 'trill.trillHeader.oplen',
        'Hop Count': 'trill.trillHeader.hpcnt',
        'Egress RBridge Nickname': 'trill.trillHeader.erbridge',
        'Ingress RBridge Nickname': 'trill.trillHeader.irbridge',
        'TRILL options': 'trill.trillHeader.options',
    }

    def __init__(self, parent):
        super(TRILL, self).__init__(parent)

    @property
    def Version(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Version']))

    @property
    def Reserved(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Reserved']))

    @property
    def Multi_Destination(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Multi Destination']))

    @property
    def Options_Length(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Options Length']))

    @property
    def Hop_Count(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Hop Count']))

    @property
    def Egress_RBridge_Nickname(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Egress RBridge Nickname']))

    @property
    def Ingress_RBridge_Nickname(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Ingress RBridge Nickname']))

    @property
    def TRILL_options(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TRILL options']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
