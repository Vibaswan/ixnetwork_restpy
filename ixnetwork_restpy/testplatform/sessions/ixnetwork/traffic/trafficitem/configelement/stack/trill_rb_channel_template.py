from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class TRILL_RB_Channel(Base):
    __slots__ = ()
    _SDM_NAME = 'trill_rb_channel'
    _SDM_ATT_MAP = {
        'Version': 'trill_rb_channel.header.version',
        'Channel Protocol': 'trill_rb_channel.header.rbridge_channel_protocol',
        'Flags': 'trill_rb_channel.header.flags',
        'ERR': 'trill_rb_channel.header.err',
    }

    def __init__(self, parent):
        super(TRILL_RB_Channel, self).__init__(parent)

    @property
    def Version(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Version']))

    @property
    def Channel_Protocol(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Channel Protocol']))

    @property
    def Flags(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Flags']))

    @property
    def ERR(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ERR']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
