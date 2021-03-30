from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class HTTP_Get(Base):
    __slots__ = ()
    _SDM_NAME = 'HTTP_GET'
    _SDM_ATT_MAP = {
        'Request': 'HTTP_GET.header.Request',
        'Host': 'HTTP_GET.header.Host',
        'User-Agent': 'HTTP_GET.header.User-Agent',
        'Accept': 'HTTP_GET.header.Accept',
        'Accept-Language': 'HTTP_GET.header.Accept-Language',
        'Accept-Encoding': 'HTTP_GET.header.Accept-Encoding',
        'Accept-Charset': 'HTTP_GET.header.Accept-Charset',
        'Keep-Alive': 'HTTP_GET.header.Keep-Alive',
        'Connection': 'HTTP_GET.header.Connection',
        'Referer': 'HTTP_GET.header.Referer',
        'CRLF': 'HTTP_GET.header.CRLF',
    }

    def __init__(self, parent):
        super(HTTP_Get, self).__init__(parent)

    @property
    def Request(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Request']))

    @property
    def Host(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Host']))

    @property
    def User_Agent(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['User-Agent']))

    @property
    def Accept(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Accept']))

    @property
    def Accept_Language(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Accept-Language']))

    @property
    def Accept_Encoding(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Accept-Encoding']))

    @property
    def Accept_Charset(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Accept-Charset']))

    @property
    def Keep_Alive(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Keep-Alive']))

    @property
    def Connection(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Connection']))

    @property
    def Referer(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Referer']))

    @property
    def CRLF(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CRLF']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
