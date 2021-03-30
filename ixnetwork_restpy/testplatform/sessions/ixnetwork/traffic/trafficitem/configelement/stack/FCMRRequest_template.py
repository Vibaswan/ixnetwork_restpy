from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class FC_MR_Request(Base):
    __slots__ = ()
    _SDM_NAME = 'FCMRRequest'
    _SDM_ATT_MAP = {
        'FC Header': 'fcMRRequest.header.fcHeader',
        'FC Command': 'fcMRRequest.header.fcCmd',
        'Reserved1': 'fcMRRequest.header.reserved1',
        'Protocol Version': 'fcMRRequest.header.version',
        'Payload': 'fcMRRequest.header.length',
    }

    def __init__(self, parent):
        super(FC_MR_Request, self).__init__(parent)

    @property
    def FC_Header(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FC Header']))

    @property
    def FC_Command(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FC Command']))

    @property
    def Reserved1(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Reserved1']))

    @property
    def Protocol_Version(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Protocol Version']))

    @property
    def Payload(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Payload']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
