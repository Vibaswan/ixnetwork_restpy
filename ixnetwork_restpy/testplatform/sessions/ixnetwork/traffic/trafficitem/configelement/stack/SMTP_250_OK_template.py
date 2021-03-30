from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class SMTP_250_OK(Base):
    __slots__ = ()
    _SDM_NAME = 'SMTP_250_OK'
    _SDM_ATT_MAP = {
        'Response Code': 'SMTP_250_OK.Response_.Response Code',
        'Space11': 'SMTP_250_OK.Response_.Space11',
        'Response parameter': 'SMTP_250_OK.Response_.Response parameter',
        'CRLF11': 'SMTP_250_OK.Response_.CRLF11',
    }

    def __init__(self, parent):
        super(SMTP_250_OK, self).__init__(parent)

    @property
    def Response_Code(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Response Code']))

    @property
    def Space11(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Space11']))

    @property
    def Response_parameter(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Response parameter']))

    @property
    def CRLF11(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CRLF11']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
