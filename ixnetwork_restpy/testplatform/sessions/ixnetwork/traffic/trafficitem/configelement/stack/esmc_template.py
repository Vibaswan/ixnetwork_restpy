from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class ESMC(Base):
    __slots__ = ()
    _SDM_NAME = 'esmc'
    _SDM_ATT_MAP = {
        'Slow protocol subtype': 'esmc.packet.subtype',
        'ITU-OUI': 'esmc.packet.ituoui',
        'ITU Subtype': 'esmc.packet.itusubtype',
        'Version': 'esmc.packet.version',
        'Event flag': 'esmc.packet.event_flag',
        'Reserved': 'esmc.packet.reserved',
        'QL-TLV': 'esmc.packet.qltlv',
        'Ext-QL-TLV': 'esmc.packet.extqltlv',
    }

    def __init__(self, parent):
        super(ESMC, self).__init__(parent)

    @property
    def Slow_protocol_subtype(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Slow protocol subtype']))

    @property
    def ITU_OUI(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ITU-OUI']))

    @property
    def ITU_Subtype(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ITU Subtype']))

    @property
    def Version(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Version']))

    @property
    def Event_flag(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Event flag']))

    @property
    def Reserved(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Reserved']))

    @property
    def QL_TLV(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['QL-TLV']))

    @property
    def Ext_QL_TLV(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Ext-QL-TLV']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
