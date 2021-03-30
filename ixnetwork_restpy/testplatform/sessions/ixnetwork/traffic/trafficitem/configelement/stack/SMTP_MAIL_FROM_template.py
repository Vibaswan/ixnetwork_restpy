from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class SMTP_MAIL_FROM(Base):
    __slots__ = ()
    _SDM_NAME = 'SMTP_MAIL_FROM'
    _SDM_ATT_MAP = {
        'Command_MAIL': 'SMTP_MAIL_FROM.Request_MAIL_FROM.field0',
        'Space10': 'SMTP_MAIL_FROM.Request_MAIL_FROM.Space10',
        'Request_FROM': 'SMTP_MAIL_FROM.Request_MAIL_FROM.Request_FROM',
        'CRLF__': 'SMTP_MAIL_FROM.Request_MAIL_FROM.CRLF__',
    }

    def __init__(self, parent):
        super(SMTP_MAIL_FROM, self).__init__(parent)

    @property
    def Command_MAIL(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Command_MAIL']))

    @property
    def Space10(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Space10']))

    @property
    def Request_FROM(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Request_FROM']))

    @property
    def CRLF__(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CRLF__']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
