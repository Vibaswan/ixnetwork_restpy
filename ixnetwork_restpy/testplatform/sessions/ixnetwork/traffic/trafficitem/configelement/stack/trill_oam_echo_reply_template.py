from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class TRILL_OAM_Echo_Reply(Base):
    __slots__ = ()
    _SDM_NAME = 'trill_oam_echo_reply'
    _SDM_ATT_MAP = {
        'SPID': 'trill_oam_echo_reply.header.spid',
        'Sequence Number': 'trill_oam_echo_reply.header.sequence',
        'TLV Total Length': 'trill_oam_echo_reply.header.tlv_total_length',
        'TLV header': 'trill_oam_echo_reply.header.',
    }

    def __init__(self, parent):
        super(TRILL_OAM_Echo_Reply, self).__init__(parent)

    @property
    def SPID(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SPID']))

    @property
    def Sequence_Number(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Sequence Number']))

    @property
    def TLV_Total_Length(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TLV Total Length']))

    @property
    def TLV_header(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TLV header']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
