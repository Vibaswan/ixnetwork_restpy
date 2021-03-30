from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class LACP(Base):
    __slots__ = ()
    _SDM_NAME = 'lacpWithoutEthernet'
    _SDM_ATT_MAP = {
        'LACP Header': 'lacpWithoutEthernet.header.header',
        'Actor Information': 'lacpWithoutEthernet.header.actor',
        'Partner Information': 'lacpWithoutEthernet.header.partner',
        'Collector Information': 'lacpWithoutEthernet.header.collector',
        'Terminator': 'lacpWithoutEthernet.header.terminator',
        'Reserved': 'lacpWithoutEthernet.header.reserved',
        'Frame Check Sequence CRC-32': 'lacpWithoutEthernet.header.fcs',
    }

    def __init__(self, parent):
        super(LACP, self).__init__(parent)

    @property
    def LACP_Header(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LACP Header']))

    @property
    def Actor_Information(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Actor Information']))

    @property
    def Partner_Information(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Partner Information']))

    @property
    def Collector_Information(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Collector Information']))

    @property
    def Terminator(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Terminator']))

    @property
    def Reserved(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Reserved']))

    @property
    def Frame_Check_Sequence_CRC_32(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Frame Check Sequence CRC-32']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
