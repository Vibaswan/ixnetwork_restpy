from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class HTTP_200_OK(Base):
    __slots__ = ()
    _SDM_NAME = 'HTTP_200_OK'
    _SDM_ATT_MAP = {
        'Response': 'HTTP_200_OK.header.fieldHolder0',
        'Date': 'HTTP_200_OK.header.Date',
        'Server': 'HTTP_200_OK.header.Server',
        'Last-Modified': 'HTTP_200_OK.header.Last-Modified',
        'ETag': 'HTTP_200_OK.header.ETag',
        'Accept-Ranges': 'HTTP_200_OK.header.Accept-Ranges',
        'Content-Length': 'HTTP_200_OK.header.Content-Length',
        'Keep-Alive': 'HTTP_200_OK.header.Keep-Alive',
        'Connection': 'HTTP_200_OK.header.Connection',
        'Content-Type': 'HTTP_200_OK.header.Content-Type',
        'CRLF': 'HTTP_200_OK.header.CRLF',
    }

    def __init__(self, parent):
        super(HTTP_200_OK, self).__init__(parent)

    @property
    def Response(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Response']))

    @property
    def Date(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Date']))

    @property
    def Server(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Server']))

    @property
    def Last_Modified(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Last-Modified']))

    @property
    def ETag(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ETag']))

    @property
    def Accept_Ranges(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Accept-Ranges']))

    @property
    def Content_Length(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Content-Length']))

    @property
    def Keep_Alive(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Keep-Alive']))

    @property
    def Connection(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Connection']))

    @property
    def Content_Type(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Content-Type']))

    @property
    def CRLF(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CRLF']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
