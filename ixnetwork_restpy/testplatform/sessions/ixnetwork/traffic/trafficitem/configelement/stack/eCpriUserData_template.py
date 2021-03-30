from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class eCPRI_User_Data(Base):
    __slots__ = ()
    _SDM_NAME = 'eCpriUserData'
    _SDM_ATT_MAP = {
        'Length': 'eCpriUserData.header.length',
        'Data': 'eCpriUserData.header.data',
    }

    def __init__(self, parent):
        super(eCPRI_User_Data, self).__init__(parent)

    @property
    def Length(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Length']))

    @property
    def Data(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Data']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
