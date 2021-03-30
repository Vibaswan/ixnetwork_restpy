from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class SNAP(Base):
    __slots__ = ()
    _SDM_NAME = 'snap'
    _SDM_ATT_MAP = {
        'SNAP OUI (Organizationally Unique Id)': 'snap.snapHeader.snapOUI',
        'SNAP PID': 'snap.snapHeader.snapPID',
    }

    def __init__(self, parent):
        super(SNAP, self).__init__(parent)

    @property
    def SNAP_OUI_Organizationally_Unique_Id(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SNAP OUI (Organizationally Unique Id)']))

    @property
    def SNAP_PID(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SNAP PID']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
