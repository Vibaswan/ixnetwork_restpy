from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class LLC_SNAP(Base):
    __slots__ = ()
    _SDM_NAME = 'llcSNAP'
    _SDM_ATT_MAP = {
        'DSAP': 'llcSNAP.snapHeader.dsap',
        'SSAP': 'llcSNAP.snapHeader.ssap',
        'Control field': 'llcSNAP.snapHeader.controlField',
        'SNAP OUI (Organizationally Unique Id)': 'llcSNAP.snapHeader.snapOUI',
        'SNAP PID': 'llcSNAP.snapHeader.snapPID',
    }

    def __init__(self, parent):
        super(LLC_SNAP, self).__init__(parent)

    @property
    def DSAP(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DSAP']))

    @property
    def SSAP(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SSAP']))

    @property
    def Control_field(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Control field']))

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
