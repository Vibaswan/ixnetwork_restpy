from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class RTSP_Reply(Base):
    __slots__ = ()
    _SDM_NAME = 'RTSP_Reply'
    _SDM_ATT_MAP = {
        'RESPONSE': 'RTSP_Reply.header.RESPONSE',
        'DATE': 'RTSP_Reply.header.DATE',
        'CSeq': 'RTSP_Reply.header.CSeq',
        'Server': 'RTSP_Reply.header.Server',
        'Supported': 'RTSP_Reply.header.Supported',
        'CRLFX': 'RTSP_Reply.header.CRLFX',
    }

    def __init__(self, parent):
        super(RTSP_Reply, self).__init__(parent)

    @property
    def RESPONSE(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RESPONSE']))

    @property
    def DATE(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DATE']))

    @property
    def CSeq(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CSeq']))

    @property
    def Server(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Server']))

    @property
    def Supported(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Supported']))

    @property
    def CRLFX(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CRLFX']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
