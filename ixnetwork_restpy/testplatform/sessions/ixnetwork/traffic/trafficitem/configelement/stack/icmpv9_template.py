from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class ICMP_Msg_Type__9(Base):
    __slots__ = ()
    _SDM_NAME = 'icmpv9'
    _SDM_ATT_MAP = {
        'Type': 'icmpv9.icmp9.type',
        'Code': 'icmpv9.icmp9.code',
        'Checksum': 'icmpv9.icmp9.checksum',
        'Num Addr': 'icmpv9.icmp9.numAddr',
        'Add Entry Size': 'icmpv9.icmp9.entrySize',
        'LifeTime': 'icmpv9.icmp9.lifetime',
        'Router Address Entries': 'icmpv9.icmp9.addressEntries',
        'TLV': 'icmpv9.icmp9.tlv',
    }

    def __init__(self, parent):
        super(ICMP_Msg_Type__9, self).__init__(parent)

    @property
    def Type(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Type']))

    @property
    def Code(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Code']))

    @property
    def Checksum(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Checksum']))

    @property
    def Num_Addr(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Num Addr']))

    @property
    def Add_Entry_Size(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Add Entry Size']))

    @property
    def LifeTime(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LifeTime']))

    @property
    def Router_Address_Entries(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Router Address Entries']))

    @property
    def TLV(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TLV']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
