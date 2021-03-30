from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class ECP(Base):
    __slots__ = ()
    _SDM_NAME = 'ecp'
    _SDM_ATT_MAP = {
        'Version': 'ecp.ecp_packet.ecpVersion',
        'Operation Type': 'ecp.ecp_packet.evbOperation',
        'Subtype': 'ecp.ecp_packet.evbSubtype',
        'Sequence Number': 'ecp.ecp_packet.ecpSequenceNo',
        'VDP Entries': 'ecp.ecp_packet.vdpEntries',
    }

    def __init__(self, parent):
        super(ECP, self).__init__(parent)

    @property
    def Version(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Version']))

    @property
    def Operation_Type(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Operation Type']))

    @property
    def Subtype(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Subtype']))

    @property
    def Sequence_Number(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Sequence Number']))

    @property
    def VDP_Entries(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['VDP Entries']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
