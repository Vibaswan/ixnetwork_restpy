from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class ATM_Cell(Base):
    __slots__ = ()
    _SDM_NAME = 'atmCell'
    _SDM_ATT_MAP = {
        'VPI': 'atmCell.atmCell.vpi',
        'VCI': 'atmCell.atmCell.vci',
        'PTI': 'atmCell.atmCell.pti',
        'Cell Relay Cbit': 'atmCell.atmCell.cellRelayCbit',
        'Cell Data': 'atmCell.atmCell.cellData',
    }

    def __init__(self, parent):
        super(ATM_Cell, self).__init__(parent)

    @property
    def VPI(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['VPI']))

    @property
    def VCI(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['VCI']))

    @property
    def PTI(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PTI']))

    @property
    def Cell_Relay_Cbit(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Cell Relay Cbit']))

    @property
    def Cell_Data(self):
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Cell Data']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
