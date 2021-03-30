from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Cisco_HDLC(Base):
    __slots__ = ()
    _SDM_NAME = 'ciscoHDLC'
    _SDM_ATT_MAP = {
        'Cisco HDLC Address': 'ciscoHDLC.header.address',
        'Cisco HDLC Control': 'ciscoHDLC.header.control',
        'Cisco HDLC Protocol Type': 'ciscoHDLC.header.protocolType',
        'Cisco CLNS Pad': 'ciscoHDLC.header.clnsPad',
    }

    def __init__(self, parent):
        super(Cisco_HDLC, self).__init__(parent)

    @property
    def Cisco_HDLC_Address(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Cisco HDLC Address']))

    @property
    def Cisco_HDLC_Control(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Cisco HDLC Control']))

    @property
    def Cisco_HDLC_Protocol_Type(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Cisco HDLC Protocol Type']))

    @property
    def Cisco_CLNS_Pad(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Cisco CLNS Pad']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
