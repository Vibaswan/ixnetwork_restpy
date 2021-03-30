from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class RTSP_DESCRIBE(Base):
    __slots__ = ()
    _SDM_NAME = 'RTSP_DESCRIBE'
    _SDM_ATT_MAP = {
        'REQUEST': 'RTSP_DESCRIBE.header.REQUEST',
        'User-Agent': 'RTSP_DESCRIBE.header.User-Agent',
        'Accept': 'RTSP_DESCRIBE.header.Accept',
        'Accept-Charset': 'RTSP_DESCRIBE.header.Accept-Charset',
        'X-Accept-Authentication': 'RTSP_DESCRIBE.header.X-Accept-Authentication',
        'Accept-Language': 'RTSP_DESCRIBE.header.Accept-Language',
        'CSeq': 'RTSP_DESCRIBE.header.CSeq',
        'Supported': 'RTSP_DESCRIBE.header.Supported',
        'CRLF': 'RTSP_DESCRIBE.header.CRLF',
    }

    def __init__(self, parent):
        super(RTSP_DESCRIBE, self).__init__(parent)

    @property
    def REQUEST(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['REQUEST']))

    @property
    def User_Agent(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['User-Agent']))

    @property
    def Accept(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Accept']))

    @property
    def Accept_Charset(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Accept-Charset']))

    @property
    def X_Accept_Authentication(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['X-Accept-Authentication']))

    @property
    def Accept_Language(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Accept-Language']))

    @property
    def CSeq(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CSeq']))

    @property
    def Supported(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Supported']))

    @property
    def CRLF(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CRLF']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
