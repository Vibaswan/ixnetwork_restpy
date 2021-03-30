from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class MLDv2_Report(Base):
    __slots__ = ()
    _SDM_NAME = 'mldv2Report'
    _SDM_ATT_MAP = {
    }

    def __init__(self, parent):
        super(MLDv2_Report, self).__init__(parent)

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
