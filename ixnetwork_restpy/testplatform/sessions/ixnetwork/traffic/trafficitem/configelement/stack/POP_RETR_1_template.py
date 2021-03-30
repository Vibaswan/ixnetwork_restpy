from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class POP_RETR_1(Base):
    __slots__ = ()
    _SDM_NAME = 'POP_RETR_1'
    _SDM_ATT_MAP = {
        'Request command': 'POP_RETR_1.REQUESTX.Request command',
        'Space7': 'POP_RETR_1.REQUESTX.Space7',
        'Request parameter': 'POP_RETR_1.REQUESTX.Request parameter',
        'CRLFxx': 'POP_RETR_1.REQUESTX.CRLFxx',
    }

    def __init__(self, parent):
        super(POP_RETR_1, self).__init__(parent)

    @property
    def Request_command(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Request command']))

    @property
    def Space7(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Space7']))

    @property
    def Request_parameter(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Request parameter']))

    @property
    def CRLFxx(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CRLFxx']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
