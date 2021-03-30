from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class ICMPv6(Base):
    __slots__ = ()
    _SDM_NAME = 'icmpv6'
    _SDM_ATT_MAP = {
        'ICMPv6 Message Type': 'icmpv6.icmpv6Message.icmpv6MessegeType',
    }

    def __init__(self, parent):
        super(ICMPv6, self).__init__(parent)

    @property
    def ICMPv6_Message_Type(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ICMPv6 Message Type']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
