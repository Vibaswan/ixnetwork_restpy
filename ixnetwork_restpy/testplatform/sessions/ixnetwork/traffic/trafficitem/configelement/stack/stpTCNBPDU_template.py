from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class STP_TCN_BPDU(Base):
    __slots__ = ()
    _SDM_NAME = 'stpTCNBPDU'
    _SDM_ATT_MAP = {
        'Protocol identifier': 'stpTCNBPDU.header.protocolIdentifier',
        'Protocol version identifier': 'stpTCNBPDU.header.protocolVersionIdentifier',
        'BPDU type': 'stpTCNBPDU.header.bpduType',
    }

    def __init__(self, parent):
        super(STP_TCN_BPDU, self).__init__(parent)

    @property
    def Protocol_identifier(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Protocol identifier']))

    @property
    def Protocol_version_identifier(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Protocol version identifier']))

    @property
    def BPDU_type(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BPDU type']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
