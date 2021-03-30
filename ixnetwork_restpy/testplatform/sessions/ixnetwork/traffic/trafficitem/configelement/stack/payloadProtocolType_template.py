from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Payload_Protocol_Type(Base):
    __slots__ = ()
    _SDM_NAME = 'payloadProtocolType'
    _SDM_ATT_MAP = {
        'Payload Protocol Id (EtherType)': 'payloadProtocolType.header.payloadProtocolId',
    }

    def __init__(self, parent):
        super(Payload_Protocol_Type, self).__init__(parent)

    @property
    def Payload_Protocol_Id_EtherType(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Payload Protocol Id (EtherType)']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
