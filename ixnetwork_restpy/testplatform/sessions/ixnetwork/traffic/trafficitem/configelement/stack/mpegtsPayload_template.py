from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class MPEG2TS_Payload(Base):
    __slots__ = ()
    _SDM_NAME = 'mpegtsPayload'
    _SDM_ATT_MAP = {
        'Length': 'mpegtsPayload.payload.length',
        'Data Payload': 'mpegtsPayload.payload.dataPayload',
    }

    def __init__(self, parent):
        super(MPEG2TS_Payload, self).__init__(parent)

    @property
    def Length(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Length']))

    @property
    def Data_Payload(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Data Payload']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
