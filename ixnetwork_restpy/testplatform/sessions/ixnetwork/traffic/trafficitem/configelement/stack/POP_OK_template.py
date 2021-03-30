from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class POP_OK(Base):
    __slots__ = ()
    _SDM_NAME = 'POP_OK'
    _SDM_ATT_MAP = {
        'Response Indicator': 'POP_OK.RESPONSE_OK.Response Indicator',
        'Space8': 'POP_OK.RESPONSE_OK.Space8',
        'Response description': 'POP_OK.RESPONSE_OK.Response description',
        'CRLF_': 'POP_OK.RESPONSE_OK.CRLF_',
    }

    def __init__(self, parent):
        super(POP_OK, self).__init__(parent)

    @property
    def Response_Indicator(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Response Indicator']))

    @property
    def Space8(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Space8']))

    @property
    def Response_description(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Response description']))

    @property
    def CRLF_(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CRLF_']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
