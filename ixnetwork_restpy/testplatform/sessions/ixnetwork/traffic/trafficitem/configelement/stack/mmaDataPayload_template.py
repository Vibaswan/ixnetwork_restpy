from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class MMA_Data_Payload(Base):
    __slots__ = ()
    _SDM_NAME = 'mmaDataPayload'
    _SDM_ATT_MAP = {
        'Length': 'mmaDataPayload.payload.length',
        'Data Payload': 'mmaDataPayload.payload.dataPayload',
    }

    def __init__(self, parent):
        super(MMA_Data_Payload, self).__init__(parent)

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
