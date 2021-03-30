from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class VIC(Base):
    __slots__ = ()
    _SDM_NAME = 'vic'
    _SDM_ATT_MAP = {
        'VIC PDU Header': 'vic.header.vicPduHeader',
        'VIC Message Types': 'vic.header.messageTypes',
    }

    def __init__(self, parent):
        super(VIC, self).__init__(parent)

    @property
    def VIC_PDU_Header(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['VIC PDU Header']))

    @property
    def VIC_Message_Types(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['VIC Message Types']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
